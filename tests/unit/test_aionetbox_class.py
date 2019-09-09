"""
module docstring
"""
import pytest
import asynctest
from mock import MagicMock
from mock import patch

from aio_netbox.client import AIONetbox


class TestAIONetboxClient():
    """ Netbox AIOHTTP Client tests """

    def test_url_builder(self):
        """ Test that we get what we expect from our inputs when building the
        URL"""

        tclient = AIONetbox(host='localhost', auth_token='mytoken')
        assert tclient._build_url('/dcim/foo') == 'localhost/api/dcim/foo'


    def test_url_builder_with_bunk_route(self):
        """ test with a missing forward slash in the route """

        tclient = AIONetbox(host='localhost', auth_token='mytoken')
        assert tclient._build_url('dcim/foo') == 'localhost/api/dcim/foo'


    def test_url_builder_with_kwarg_valid_params(self):
        """ test with key/value pairs that should be serialized into url params
        """

        tclient = AIONetbox(host='localhost', auth_token='mytoken')
        assert tclient._build_url('dcim/foo', foo='bar') == 'localhost/api/dcim/foo?foo=bar'


    def test_url_builder_with_kwarg_invalid_params(self):
        """ test with key/value pairs that should be serialized into url params
        """

        tclient = AIONetbox(host='localhost', auth_token='mytoken')
        assert tclient._build_url('dcim/foo', invalid='') == 'localhost/api/dcim/foo?invalid='

    @pytest.mark.asyncio
    async def test_get_passes_auth_token(self):
        """ stuff and things """
        with patch.object(AIONetbox, 'client', return_value = asynctest.MagicMock()) as aiobutts:
            tclient = AIONetbox(host='localhost', auth_token='mytoken')
            print(tclient.client)
            resp = await tclient.get('dcim/foo')
            print(resp)

