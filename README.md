# AIO Netbox

An asyncio netbox library that conforms to any running netbox via it's OpenAPI spec

## Usage

```
from aionetbox import AIONetbox

netbox = AIONetbox.from_openapi(
    url='http://localhost:8000',
    api_key='0123abcd'
)

sites = await netbox.dcim.dcim_sites_list()
my_site = await netbox.dcim.dcim_sites_read(id=2)

custom_field_sort = await netbox.dcim.dcim_regions_list(cf_sf_id='identifier')
```

Each module and method map to the swagger definition for netbox (`/api/docs`)

![](https://imgur.com/Mhs4UHz.png)
