"""
here's a docstring
"""

import asyncio
import aiohttp

# AIOHTTP request helper
class AIONetbox():
    """AIONetbox

    An AIOHTTP client implementation for Netbox. Specifically with an eye
    towards non-blocking client requests.

    Todo:
            * retry-logic
            * exception catching
    """

    def __init__(self, *, host=None, port=None, auth_token=None, loop=None):
        self.host = host
        self.port = port
        self.auth_token = auth_token
        self.loop = loop or asyncio.get_event_loop()
        self._client = None

    def client(self):
        """
        An AIO HTTP request client factory for interfacing with netbox
        """
        if not self._client:
            self._client = aiohttp.ClientSession()

        return self._client


    def _build_url(self, route, **kwargs):
        """
          _build_url - concatenate details to build the netbox path to query
        """
        # Route will be kind to the user and prepend the / if omitted
        if not route.startswith('/'):
            route = '/{}'.format(route)

        # build the base url
        url = '{}{}/api{}'.format(self.host,
                                  ':{}'.format(self.port) if self.port
                                  else '', route)

        # convert key=value pairs into URL parameters
        if kwargs:
            url = '{}?{}'.format(url,
                                 '&'.join('{}={}'.format(key, val) \
                                          for key, val in kwargs.items()))
        return url


    async def get(self, route, **kwargs):
        """
        get - the outer method to invoke the actual http request

        TODO: Make this invoke a __fetch_all() method that knows how to
        speak the pagination of netbox so we're dealing with flat frames
        of data
        """
        headers = {'Authorization': 'Token {}'.format(self.auth_token),
                   'content-type': 'text/plain'}

        url = self._build_url(route, **kwargs)

        async with self.client().get(url, headers=headers) as resp:
            body = await resp.json(content_type='application/json')
            if 'results' in body.keys():
                return body['results']
            else:
                raise ValueError("Did not receive the data we expected")


    async def close(self):
        """
        close the socket connection
        """
        await self.client().close()
