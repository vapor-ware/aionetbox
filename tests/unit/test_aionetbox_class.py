import pytest

from aio_netbox import AIONetbox

class TestAIONetboxClient(object):
    """ Netbox AIOHTTP Client tests """

    def test_query_lockers(self):
        """ Test retrieval of lockers """
        tclient = AIONetbox(host="localhost", auth_token="TEST1234")

