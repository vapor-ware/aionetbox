"""
Integration test suite

Target a sandboxed version of netbox and run full http queries to
test all of the constituent components function as expected.

"""
import pytest
import asynctest
import os
from asynctest import patch

from mock import MagicMock

from aionetbox.client import AIONetbox
from aionetbox.exceptions import NoResultsException


class TestAIONetboxIntegration():
    """ Netbox AIOHTTP Client tests """

    @classmethod
    def fixed_client(cls):
        """ DRY Fixture to have a consistently configured AIONetbox client """
        host = os.getenv('NETBOX_INTEGRATION_HOST')
        auth_token = os.getenv('NETBOX_INTEGRATION_TOKEN')
        return AIONetbox(host=host, auth_token=auth_token)


    @pytest.mark.asyncio
    async def test_get_all_customers(self):
        # https://netbox/api/vapor/customers/
        client = self.fixed_client()
        resp = await client.get('vapor/customers')
        assert len(resp) > 0
        assert 'name' in resp[0].keys()
        assert 'slug' in resp[0].keys()
        assert 'devices' in resp[0].keys()

   

    @pytest.mark.asyncio
    async def test_get_single_customer(self):
        # https://netbox/api/vapor/customers/?slug=customer1
        client = self.fixed_client()
        resp = await client.get('vapor/customers', slug='customer1')
        assert resp[0]['name'] == 'customer1'



    @pytest.mark.asyncio
    async def test_get_customer_interfaces(self):
        # https://netbox/api/vapor/customers/?slug=customer1
        client = self.fixed_client()
        resp = await client.get('vapor/customers', slug='customer1')
        assert resp[0]['name'] == 'customer1'


