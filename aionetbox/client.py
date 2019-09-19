import asyncio
import aiohttp
from aionetbox.decorators import retry_request
from aionetbox.exceptions import NoResultsException


# AIOHTTP request helper
class AIONetbox():
    """AIONetbox

    An AIOHTTP client implementation for Netbox. Specifically with an eye
    towards non-blocking client requests.

    TODOS:
    -  Make get invoke a __fetch_all() method that knows how to
    speak the pagination of netbox. Today we don't have enough data to test.
    """

    def __init__(self, *, host=None, port=None, auth_token=None, loop=None):
        self.host = host
        self.port = port
        self.auth_token = auth_token
        self.loop = loop or asyncio.get_event_loop()
        self.client = None

    def _init_client(self):
        """ Initialize the client provisioning a new one if a previous
        client has not been cached
        """
        if not self.client:
            self.client = aiohttp.ClientSession()


    def _build_url(self, route):
        """ concatenate params to build the netbox API path to query
        Args:
            route - the path segment after /api, eg: '/dcim/devices'
            kwargs - key,val pairs to be urlencoded as parameters.
        Returns:
            url: a string representation of the full url.
        """

        # note: bump with 110 from edge_monitor

        # Route will be kind to the user and prepend the / if omitted
        if not route.startswith('/'):
            route = '/{}'.format(route)

        # build the base url
        return '{}{}/api{}'.format(self.host,
                                   ':{}'.format(self.port) if self.port
                                   else '', route)


    @retry_request(exceptions=(aiohttp.ClientError, asyncio.TimeoutError))
    async def get(self, route, **kwargs):
        """ Invoke an http get against the netbox api
        Args:
            route - the path segment after /api, eg: '/dcim/devices'
            kwargs - key,val pairs to be urlencoded as parameters.
        Returns:
            body['results']: the json blob representing the devices queried
            from netbox.
        Raises:
            NoResultsException - the 'results' key is not present in the json
            body. Which is a convention of netbox.

        """
        headers = {'Authorization': 'Token {}'.format(self.auth_token),
                   'content-type': 'application/json'}

        url = self._build_url(route)
        self._init_client()

        async with self.client.get(url, headers=headers, params=kwargs) as resp:
            body = await resp.json(content_type='application/json')
            if not 'results' in body:
                msg = 'expected key "results" not found in response body'
                raise NoResultsException(msg)

            return body['results']


    @retry_request(exceptions=(aiohttp.ClientError, asyncio.TimeoutError))
    async def post(self, route, payload=None, **kwargs):
        """ Invoke an http post against the netbox api
        Args:
            route - the path segment after /api, eg: '/dcim/devices'
            kwargs - key,val pairs to be urlencoded as parameters.
        Returns:
            body: the json blob representing the creation of a resource in netbox

        """
        headers = {'Authorization': 'Token {}'.format(self.auth_token),
                   'content-type': 'application/json'}

        url = self._build_url(route)
        self._init_client()

        async with self.client.post(url, headers=headers, params=kwargs,
                                    payload=payload) as resp:
            body = await resp.json(content_type='application/json')
            return body



    async def close(self):
        """close the http socket connection
        """
        await self.client.close()
