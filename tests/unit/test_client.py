"""
module docstring
"""
import pytest
import asynctest
from asynctest import patch

from mock import MagicMock

from aionetbox.client import AIONetbox
from aionetbox.exceptions import NoResultsException


class TestAIONetboxClient():
    """ Netbox AIOHTTP Client tests """

    @patch('aiohttp.ClientSession')
    def test_init_client(self, msess):
        """ Test  if it will create a AIOHTTP client if self.client has not
        been set """
        tclient = AIONetbox(host='anywho', auth_token='token')
        assert tclient.client is None
        tclient._init_client()
        assert tclient.client == msess.return_value
        # ensure the client is cached
        tclient._init_client()
        assert tclient.client == msess.return_value

    def test_url_builder(self):
        """ Test that we get what we expect from our inputs when building the
        URL"""

        tclient = AIONetbox(host='localhost', auth_token='mytoken')
        assert tclient._build_url('/dcim/foo') == 'localhost/api/dcim/foo'

    def test_url_builder_with_bunk_route(self):
        """ test with a missing forward slash in the route """

        tclient = AIONetbox(host='localhost', auth_token='mytoken')
        assert tclient._build_url('dcim/foo') == 'localhost/api/dcim/foo'

    @pytest.mark.asyncio
    async def test_url_builder_with_kwarg_valid_params(self):
        """ test with key/value pairs that should be serialized into url params
        """

        tclient = AIONetbox(host='localhost', auth_token='mytoken')

        # A note about these mocks and why:
        # https://stackoverflow.com/a/48762969/196832
        mclient = asynctest.CoroutineMock()
        mclient.get.return_value.__aenter__.return_value.json = asynctest.CoroutineMock(return_value={'results': []}) # noqa

        tclient.client = mclient

        resp = await tclient.get('dcim/foo', foo='bar')
        mclient.get.assert_called_with('localhost/api/dcim/foo',
                                       headers={'Authorization': 'Token mytoken',
                                                'content-type': 'application/json'},
                                       params={'foo': 'bar'})

    @pytest.mark.asyncio
    async def test_get_passes_auth_token(self):
        """ test with authentication token and validate it is correctly
        formatted """

        tclient = AIONetbox(host='localhost', auth_token='specifictoken')

        # A note about these mocks and why:
        # https://stackoverflow.com/a/48762969/196832
        mclient = asynctest.CoroutineMock()
        mclient.get.return_value.__aenter__.return_value.json = asynctest.CoroutineMock(return_value={'results': []}) # noqa

        tclient.client = mclient

        resp = await tclient.get('dcim/foo')
        mclient.get.assert_called_with('localhost/api/dcim/foo',
                                       headers={'Authorization': 'Token specifictoken',
                                                'content-type': 'application/json'},
                                       params={})

    @pytest.mark.asyncio
    async def test_get_raises_exception(self):
        """ test that an exception is raised when we get a JSON result without
        the 'results' key. As this is a netbox convention/assumption """
        tclient = AIONetbox(host='localhost', auth_token='mytoken')

        # A note about these mocks and why:
        # https://stackoverflow.com/a/48762969/196832
        mclient = asynctest.CoroutineMock()
        mclient.get.return_value.__aenter__.return_value.json = asynctest.CoroutineMock(return_value={}) # noqa

        tclient.client = mclient

        with pytest.raises(NoResultsException):
            resp = await tclient.get('dcim/foo')

    @pytest.mark.asyncio
    async def test_post_function(self):
        """ test that post's are invoked with expected parameters """
        tclient = AIONetbox(host='localhost', auth_token='mytoken')

        # A note about these mocks and why:
        # https://stackoverflow.com/a/48762969/196832
        mclient = asynctest.CoroutineMock()
        mclient.post.return_value.__aenter__.return_value.json = asynctest.CoroutineMock(return_value={}) # noqa

        tclient.client = mclient

        resp = await tclient.post('/dcim/foo', payload={'update': 'data'})
        mclient.post.assert_called_with('localhost/api/dcim/foo',
                                        headers={'Authorization': 'Token mytoken',
                                                'content-type': 'application/json'},
                                        params={},
                                        payload={'update': 'data'})



    @pytest.mark.asyncio
    async def test_close_client(self):
        """ validate that closing the connection """
        tclient = AIONetbox(host='anywho', auth_token='token')
        tclient.client = asynctest.MagicMock()
        tclient.client.close = asynctest.CoroutineMock()
        # ensure the client is cached
        await tclient.close()
