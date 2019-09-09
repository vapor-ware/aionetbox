import os
import asyncio
import aiohttp
import json

# AIOHTTP request helper
class AIONetbox(object):
    def __init__(self, *, host=None, port=None, auth_token=None, loop=None):
        self.host = host
        self.port = port
        self.auth_token = auth_token
        self.loop = loop or asyncio.get_event_loop()
        self._client = None

    def client(self):
        if not self._client:
            self._client = aiohttp.ClientSession()

        return self._client

    def _build_url(self, route, **kwargs):
        return '{}{}/api{}'.format(self.host, ':{}'.format(self.port) if self.port else '', route)

    async def get(self, route, **kwargs):
        # TODO: Make this invoke a __fetdch_all() method that knows how to
        # speak the pagination of netbox so we're dealing with flat frames
        # of data
        headers = { 'Authorization': "Token {}".format(self.auth_token),
                    'content-type': "application/json"}

        # Kind of hacky but append any args as parameters to the query
        if kwargs:
          url = "{}?{}".format(self._build_url(route), '&'.join('{}={}'.format(key, val) for key, val in kwargs.items()))

        async with self.client().get(url, headers=headers) as resp:
            return (await resp.json())['results']

    async def close(self):
        await self.client().close()


# Main method
async def run(token, tenant_id=None):
    nb = AIONetbox(host='https://netbox.preview.cloud.vio.sh', auth_token=token)
    results = {}
    lockers = await nb.get('/dcim/devices', role="customer-network-locker")

    # filter for just the tenants lockers
    tenant_lockers = [x for x in lockers if (x["tenant"] != None) and (x["tenant"]["id"] == tenant_id) ]
    # With our list of lockers, we can iterate the connections to extract the network
    # devices (ports)
    short_list = [x["name"] for x in tenant_lockers]

    tenant_ports = await nb.get('/dcim/interface-connections', devices=short_list)

    for locker in lockers:
        # search through interface b, which is the customer locker interface by convention in our netbox data
        device_interfaces = [ y for y in tenant_ports if (y["interface_b"] != None) and (y["interface_b"]["device"]["id"] == locker["id"]) ]

        # Get all the network switch details
        switches = [ p["interface_a"] for p in device_interfaces if p["interface_a"] !=  None ]
        # List placeholder for the modified objects
        switches_dense = []
        tenant_ifaces = []
        # Since we query by switch id, there should only ever be 1... at least I hope.
        for switch in switches:
            iface_detail = await nb.get('/dcim/interfaces', id=switch["id"])
            # fetch the device LAG and TYPE for switches for the UI:
            switch["type"] = iface_detail[0]["type"]
            switch["lag"] = iface_detail[0]["lag"]
            switches_dense.append(switch)

        # the same logic for the client connections
        client_ifaces = [ p["interface_b"] for p in device_interfaces if p["interface_b"] != None ]
        for iface in client_ifaces:
            iface_detail = await nb.get('/dcim/interfaces', id=iface["id"])
            # fetch the device LAG and TYPE for Client Ifaces for the UI:
            iface["type"] = iface_detail[0]["type"]
            iface["lag"] = iface_detail[0]["lag"]
            tenant_ifaces.append(iface)

        # finally update our results object
        results.update({ locker["name"]: {
                     "id": locker["id"],
                     "display_name": locker["display_name"],
                     "device_type": locker["device_type"],
                     "interfaces":
                        tenant_ifaces,
                     "switches":
                        switches_dense,
                   } })




    await nb.close()
    print(json.dumps(results, indent=3))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(os.environ.get('NETBOX_TOKEN'), os.environ.get('TENANT_ID')))

