
import re
import json
import asyncio
import logging
import collections

from aionetbox.utils import singleton

from typing import Iterable

import aiohttp
from prance import ResolvingParser

from aionetbox.exceptions import (
    BadRequest,
    MissingRequiredParam,
    InvalidResponse,
    InvalidRequest,
)

log = logging.getLogger(__name__)


@singleton
class NetboxSpec(ResolvingParser):
    pass


class AIONetbox():
    """asyncio Netbox Client

    Args:
        host: Base URL of Netbox instance
        api_key: The API Token from Netbox to access Netbox API
        spec: Dictionary or ResolvingParser of OpenAPI/Swagger spec
        session: ClientSession for http requests
        loop: Optional asyncio loop
    """

    _http_methods = ('GET', 'HEAD', 'DELETE', 'POST', 'PUT', 'PATCH', 'OPTIONS')
    _api_cache = {}

    @classmethod
    def from_openapi(cls, url, api_key, session=None):
        """Create an AIONetbox using a remote OpenAPI/Swagger Specification.

        Args:
            url: Base URL with protocol to load swagger spec.
            api_key: The API Token from Netbox to access Netbox API
            session: ClientSession for http requests
        """
        spec = NetboxSpec('{}/api/swagger.json'.format(url))

        aionb = cls(url, api_key, spec=spec, session=session)

        return aionb

    @classmethod
    def from_spec(cls, spec, api_key, session=None):
        """Create an AIONetbox using an OpenAPI/Swagger Specification from disk.

        Args:
            spec: String or full path on disk of OpenAPI/Swagger spec
            api_key: The API Token from Netbox to access Netbox API
            session: ClientSession for http requests
        """
        data = NetboxSpec(spec)

        url = '{}://{}'.format(data.specification.get('schemes', ['http'])[0], data.specification.get('host'))
        aionb = cls(url, api_key, spec=data, session=session)

        return aionb

    def __init__(self, host, api_key, spec=None, session=None, loop=None):
        self.host = host
        self.api_key = api_key
        self.session = session or aiohttp.ClientSession()
        self.config = self.parse_spec(spec)
        self.tags = self.config.keys()
        self.loop = loop or asyncio.get_event_loop()

    async def request(self, method, url, query_params=None, headers=None, body=None, post_params=None, timeout=None):
        """Execute a web request

        Args:
            method: HTTP verb for request
            url: Full URL of resource for request
            query_params: Query paramemters to be added at the end of url
            headers: Additional headers for request
            body: Request body
            post_params: http form parameters
            timeout: request timeout in seconds
        """
        method = method.upper()
        assert method in self._http_methods

        if post_params and body:
            raise ValueError(
                'body parameter cannot be used with post_params parameter.'
            )

        post_params = post_params or {}
        headers = headers or {}
        headers.update({
            'Authorization': f'Token {self.api_key}',
        })
        timeout = timeout or 5 * 60

        if 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'

        args = {
            'method': method,
            'url': url,
            'timeout': timeout,
            'params': query_params,
            'headers': headers
        }

        if method in ['POST', 'PUT', 'PATCH', 'OPTIONS', 'DELETE']:
            if re.search('json', headers['Content-Type'], re.IGNORECASE):
                if body is not None:
                    body = json.dumps(body)
                args['data'] = body
            elif headers['Content-Type'] == 'application/x-www-form-urlencoded':  # noqa: E501
                args['data'] = aiohttp.FormData(post_params)

            # Pass a `bytes` parameter directly in the body to support
            # other content types than Json when `body` argument is provided
            # in serialized form
            elif isinstance(body, bytes):
                args['data'] = body
            else:
                # Cannot generate the request from given parameters
                raise InvalidRequest(
                    'Cannot prepare a request message for provided arguments. Please check that your arguments match '
                    'declared content type.'
                )

        return await self.session.request(**args)

    def parse_spec(self, config):
        """Parse OpenAPI/Swagger spec"""

        operations = {}

        if not config:
            return {}

        if isinstance(config, ResolvingParser):
            config = config.specification

        operations['_orig'] = config
        for path, data in config.get('paths', {}).items():
            for method in self._http_methods:
                action = method.lower()
                if action not in data:
                    continue

                payload = data.get(action, {})
                tags = payload.get('tags', [])

                operationId = payload.get('operationId')
                if not operationId:
                    continue

                for tag in tags:
                    if tag not in operations:
                        operations[tag] = {}

                    rest_cfg = {
                        'url': path,
                        'params': data.get('parameters', []),
                        'method': action,
                    }

                    operations[tag][operationId] = payload
                    operations[tag][operationId]['rest'] = rest_cfg

        return operations

    def __getattr__(self, tag):
        """NetboxApi Lookup

        Used when accessing a certain tag of the netbox api. The result of this method depends on what tags
        are defined in the OpenAPI/Swagger spec.
        """
        if tag not in self.tags:
            raise AttributeError("'{}' object has no attribute '{}'".format(self.__class__.__name__, tag))

        if tag in self._api_cache:
            return self._api_cache.get(tag)

        c = NetboxApi(tag, self.config.get(tag), self)
        self._api_cache[tag] = c

        return c

    async def close(self):
        """Close all open connections"""
        await self.session.close()

    def __del__(self):
        asyncio.ensure_future(self.session.close())


class NetboxApi():
    """Netbox API group endpoint

    Args:
        tag: Netbox API Group name
        operations: one or more operations
        client: AIONetbox instance
    """
    def __init__(self, tag, operations, client):
        self.name = tag
        self.config = operations
        self.operations = operations.keys()
        self.client = client

        self._operation_cache = {}

    def __getattr__(self, operation):
        """NetboxApiOperation lookup

        Used to load an operationId from configuration of the API group
        """
        if operation not in self.operations:
            raise AttributeError("'{}' object has no attribute '{}'".format(self, operation))

        if operation in self._operation_cache:
            return self._operation_cache.get(operation)

        m = NetboxApiOperation(self.name, operation, self.config.get(operation), self.client)
        self._operation_cache[operation] = m

        return m

    def __repr__(self):
        return 'Netbox.{}'.format(self.name)


class NetboxApiOperation():
    """Netbox API group operation

    Args:
        tag: Netbox API Group name
        operation: operation name
        config: Operation configuration
        client: AIONetbox instance
    """
    def __init__(self, tag, operation, config, client):
        self.client = client
        self.config = config
        self.rest_config = self.config.get('rest', {})
        self.operation = operation
        self.tag = tag

    async def request(self, **kwargs):
        """Execute a web request"""
        path, body, query = self.parse_params(kwargs)

        if self.operation_method == 'list':
            # netbox has terrible swagger spec generation and leaves out custom fields (cf)
            keys_used = set(list(body.keys()) + list(query.keys()) + list(path.keys()))
            remaining_vars = set(kwargs.keys()) - keys_used

            for kw in remaining_vars:
                if kw.startswith('cf_'):
                    query[kw] = kwargs.get(kw)

        url = self.build_url(self.rest_config.get('url')).format(**path)

        resp = await self.client.request(
            method=self.rest_config.get('method'),
            url=url,
            query_params=query,
            body=body
        )

        resp.raise_for_status()
        data = await resp.json()
        output = NetboxResponseObject.from_response(
            data=data,
            **self.config.get('responses', {}).get(str(resp.status), {}).get('schema', {})
        )

        if self.operation_method != 'list':
            return output

        while output.next:
            resp = await self.client.request(
                method=self.rest_config.get('method'),
                url=output.next
            )

            resp.raise_for_status()
            data = await resp.json()
            pagination_output = NetboxResponseObject.from_response(
                data=data,
                **self.config.get('responses', {}).get(str(resp.status), {}).get('schema', {})
            )

            output.results.extend(pagination_output.results)
            output.next = pagination_output.next

        return output

    def build_url(self, url):
        """Construct a URL from spec"""
        return '{}{}{}'.format(self.client.host, self.client.config.get('_orig', {}).get('basePath'), url)

    def parse_params(self, params):
        """Build request parameters and validate based on spec"""
        qb = {
            'body': {},
            'query': {},
            'path': {},
        }

        spec_parameters = self.config.get('parameters', []) + self.rest_config.get('params', [])
        for sp in spec_parameters:
            if sp['name'] not in params and sp['required']:
                raise MissingRequiredParam('{} is a required parameter'.format(sp['name']))

            if sp['name'] not in params:
                continue

            if sp['in'] == 'body':
                # BODY params are special in that the name is not passed through
                qb[sp['in']] = params.get(sp['name'])
            else:
                qb[sp['in']][sp['name']] = params.get(sp['name'])

        return (qb.get('path'), qb.get('body'), qb.get('query'))

    @property
    def operation_method(self):
        if self.operation.endswith('partial_update'):
            return 'partial_update'

        return self.operation.split('_')[-1]

    async def __call__(self, **kwargs):
        """ Execute given operation request

        When a user executes an instance of NetboxApiOperation those arguments will passed through to ``request``
        """
        try:
            return await self.request(**kwargs)
        except MissingRequiredParam as e:
            raise AttributeError(str(e))
        except aiohttp.ClientResponseError as e:
            raise BadRequest('{} failed with code {}: {}'.format(self.operation, e.status, e.message))

    def __repr__(self):
        return 'Netbox.{}.{}'.format(self.tag, self.operation)


class NetboxResponseObject():
    """Netbox Response

    Take the output from an ``AIONetbox.request`` and formats / validates it based on a passed spec
    """

    @classmethod
    def from_response(cls, data, **kwargs):

        if 'type' not in kwargs:
            raise AttributeError('type is a required parameter')

        output = cls()
        if kwargs['type'] != 'object':
            return data

        required = kwargs.get('required', [])
        properties = kwargs.get('properties', {})

        for req in required:
            # Check for all required response parameters
            if req not in data:
                raise InvalidResponse('Response did not include required "{}"'.format(req))

        # if type == 'array':
        #     return [] # What if the root object is an array?

        # Iterate over every datapoint and further parse if required
        for key, val in data.items():
            spec = properties.get(key, {})
            ctype = spec.get('type')
            value = val

            if ctype == 'object':
                if isinstance(val, collections.Mapping):
                    value = cls.from_response(data=val, **spec)
            elif ctype == 'array':
                # If we have an array of objects, make sure the value is iterable, then produce a list of objects
                if isinstance(val, Iterable):
                    value = [cls.from_response(data=v, **spec.get('items')) for v in val]

            setattr(output, key, value)

        return output

    def __repr__(self):
        return '{}'.format(self.__dict__)
