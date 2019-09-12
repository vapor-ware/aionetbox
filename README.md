# AIONetbox

An async web client for [Netbox](https://github.com/netbox-community/netbox)


### Note

This library currently only supports read operations. PUT/POST support will
be coming in a future release of the library.

## Installation

AIONetbox is distributed as a library intended to be included in other async
python projects. It has been developed on python 3.6+. aionetbox is published
on the cheese shop for ease of use.

installation can be as easy as:
```shell
pip install aionetbox
```

or use your virtualenv/tox tooling to guide you.

## Example Usage

The idea behind AIONetbox is not to abstract the netbox classes with assumptions
but instead offer a non-blocking client for async frameworks. its expected that
the developer consuming AIONetbox will be at least a little familiar with the
API structure of netbox. If not, the following is a good resource to use when
calculating your API routes to query:

- [API Overview](https://github.com/netbox-community/netbox/blob/develop/docs/api/overview.md)
- [Netbox Documentation](https://netbox.readthedocs.io/en/stable/)

Code Sample for a READ device scan:

```python
import asyncio
import json
from aionetbox include AIONetbox

async def run(token):
  # Initialize with the host, and your authentication token
  nbox = AIONetbox(host='https://netbox.example.com', auth_token=token)
  # Provide the api-route you wish to poll, and any key/value args
  devices = await nbox.get('/dcim/devices', role='some-role')
  # be tidy and close your connection when complete
  await nbox.close()
  print(json.dumps(devices, indent=2))

# this is setup so we have an event loop and can leverage asyncio
if __name__ == '__main__':
    LOOP = asyncio.get_event_loop()
    LOOP.run_until_complete(run('my-netbox-token'))
```

