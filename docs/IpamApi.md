# aionetbox.IpamApi

All URIs are relative to *http://ceppi.ngrok.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ipam_aggregates_create**](IpamApi.md#ipam_aggregates_create) | **POST** /ipam/aggregates/ | 
[**ipam_aggregates_delete**](IpamApi.md#ipam_aggregates_delete) | **DELETE** /ipam/aggregates/{id}/ | 
[**ipam_aggregates_list**](IpamApi.md#ipam_aggregates_list) | **GET** /ipam/aggregates/ | 
[**ipam_aggregates_partial_update**](IpamApi.md#ipam_aggregates_partial_update) | **PATCH** /ipam/aggregates/{id}/ | 
[**ipam_aggregates_read**](IpamApi.md#ipam_aggregates_read) | **GET** /ipam/aggregates/{id}/ | 
[**ipam_aggregates_update**](IpamApi.md#ipam_aggregates_update) | **PUT** /ipam/aggregates/{id}/ | 
[**ipam_choices_list**](IpamApi.md#ipam_choices_list) | **GET** /ipam/_choices/ | 
[**ipam_choices_read**](IpamApi.md#ipam_choices_read) | **GET** /ipam/_choices/{id}/ | 
[**ipam_ip_addresses_create**](IpamApi.md#ipam_ip_addresses_create) | **POST** /ipam/ip-addresses/ | 
[**ipam_ip_addresses_delete**](IpamApi.md#ipam_ip_addresses_delete) | **DELETE** /ipam/ip-addresses/{id}/ | 
[**ipam_ip_addresses_list**](IpamApi.md#ipam_ip_addresses_list) | **GET** /ipam/ip-addresses/ | 
[**ipam_ip_addresses_partial_update**](IpamApi.md#ipam_ip_addresses_partial_update) | **PATCH** /ipam/ip-addresses/{id}/ | 
[**ipam_ip_addresses_read**](IpamApi.md#ipam_ip_addresses_read) | **GET** /ipam/ip-addresses/{id}/ | 
[**ipam_ip_addresses_update**](IpamApi.md#ipam_ip_addresses_update) | **PUT** /ipam/ip-addresses/{id}/ | 
[**ipam_prefixes_available_ips_create**](IpamApi.md#ipam_prefixes_available_ips_create) | **POST** /ipam/prefixes/{id}/available-ips/ | 
[**ipam_prefixes_available_ips_read**](IpamApi.md#ipam_prefixes_available_ips_read) | **GET** /ipam/prefixes/{id}/available-ips/ | 
[**ipam_prefixes_available_prefixes_create**](IpamApi.md#ipam_prefixes_available_prefixes_create) | **POST** /ipam/prefixes/{id}/available-prefixes/ | 
[**ipam_prefixes_available_prefixes_read**](IpamApi.md#ipam_prefixes_available_prefixes_read) | **GET** /ipam/prefixes/{id}/available-prefixes/ | 
[**ipam_prefixes_create**](IpamApi.md#ipam_prefixes_create) | **POST** /ipam/prefixes/ | 
[**ipam_prefixes_delete**](IpamApi.md#ipam_prefixes_delete) | **DELETE** /ipam/prefixes/{id}/ | 
[**ipam_prefixes_list**](IpamApi.md#ipam_prefixes_list) | **GET** /ipam/prefixes/ | 
[**ipam_prefixes_partial_update**](IpamApi.md#ipam_prefixes_partial_update) | **PATCH** /ipam/prefixes/{id}/ | 
[**ipam_prefixes_read**](IpamApi.md#ipam_prefixes_read) | **GET** /ipam/prefixes/{id}/ | 
[**ipam_prefixes_update**](IpamApi.md#ipam_prefixes_update) | **PUT** /ipam/prefixes/{id}/ | 
[**ipam_rirs_create**](IpamApi.md#ipam_rirs_create) | **POST** /ipam/rirs/ | 
[**ipam_rirs_delete**](IpamApi.md#ipam_rirs_delete) | **DELETE** /ipam/rirs/{id}/ | 
[**ipam_rirs_list**](IpamApi.md#ipam_rirs_list) | **GET** /ipam/rirs/ | 
[**ipam_rirs_partial_update**](IpamApi.md#ipam_rirs_partial_update) | **PATCH** /ipam/rirs/{id}/ | 
[**ipam_rirs_read**](IpamApi.md#ipam_rirs_read) | **GET** /ipam/rirs/{id}/ | 
[**ipam_rirs_update**](IpamApi.md#ipam_rirs_update) | **PUT** /ipam/rirs/{id}/ | 
[**ipam_roles_create**](IpamApi.md#ipam_roles_create) | **POST** /ipam/roles/ | 
[**ipam_roles_delete**](IpamApi.md#ipam_roles_delete) | **DELETE** /ipam/roles/{id}/ | 
[**ipam_roles_list**](IpamApi.md#ipam_roles_list) | **GET** /ipam/roles/ | 
[**ipam_roles_partial_update**](IpamApi.md#ipam_roles_partial_update) | **PATCH** /ipam/roles/{id}/ | 
[**ipam_roles_read**](IpamApi.md#ipam_roles_read) | **GET** /ipam/roles/{id}/ | 
[**ipam_roles_update**](IpamApi.md#ipam_roles_update) | **PUT** /ipam/roles/{id}/ | 
[**ipam_services_create**](IpamApi.md#ipam_services_create) | **POST** /ipam/services/ | 
[**ipam_services_delete**](IpamApi.md#ipam_services_delete) | **DELETE** /ipam/services/{id}/ | 
[**ipam_services_list**](IpamApi.md#ipam_services_list) | **GET** /ipam/services/ | 
[**ipam_services_partial_update**](IpamApi.md#ipam_services_partial_update) | **PATCH** /ipam/services/{id}/ | 
[**ipam_services_read**](IpamApi.md#ipam_services_read) | **GET** /ipam/services/{id}/ | 
[**ipam_services_update**](IpamApi.md#ipam_services_update) | **PUT** /ipam/services/{id}/ | 
[**ipam_vlan_groups_create**](IpamApi.md#ipam_vlan_groups_create) | **POST** /ipam/vlan-groups/ | 
[**ipam_vlan_groups_delete**](IpamApi.md#ipam_vlan_groups_delete) | **DELETE** /ipam/vlan-groups/{id}/ | 
[**ipam_vlan_groups_list**](IpamApi.md#ipam_vlan_groups_list) | **GET** /ipam/vlan-groups/ | 
[**ipam_vlan_groups_partial_update**](IpamApi.md#ipam_vlan_groups_partial_update) | **PATCH** /ipam/vlan-groups/{id}/ | 
[**ipam_vlan_groups_read**](IpamApi.md#ipam_vlan_groups_read) | **GET** /ipam/vlan-groups/{id}/ | 
[**ipam_vlan_groups_update**](IpamApi.md#ipam_vlan_groups_update) | **PUT** /ipam/vlan-groups/{id}/ | 
[**ipam_vlans_create**](IpamApi.md#ipam_vlans_create) | **POST** /ipam/vlans/ | 
[**ipam_vlans_delete**](IpamApi.md#ipam_vlans_delete) | **DELETE** /ipam/vlans/{id}/ | 
[**ipam_vlans_list**](IpamApi.md#ipam_vlans_list) | **GET** /ipam/vlans/ | 
[**ipam_vlans_partial_update**](IpamApi.md#ipam_vlans_partial_update) | **PATCH** /ipam/vlans/{id}/ | 
[**ipam_vlans_read**](IpamApi.md#ipam_vlans_read) | **GET** /ipam/vlans/{id}/ | 
[**ipam_vlans_update**](IpamApi.md#ipam_vlans_update) | **PUT** /ipam/vlans/{id}/ | 
[**ipam_vrfs_create**](IpamApi.md#ipam_vrfs_create) | **POST** /ipam/vrfs/ | 
[**ipam_vrfs_delete**](IpamApi.md#ipam_vrfs_delete) | **DELETE** /ipam/vrfs/{id}/ | 
[**ipam_vrfs_list**](IpamApi.md#ipam_vrfs_list) | **GET** /ipam/vrfs/ | 
[**ipam_vrfs_partial_update**](IpamApi.md#ipam_vrfs_partial_update) | **PATCH** /ipam/vrfs/{id}/ | 
[**ipam_vrfs_read**](IpamApi.md#ipam_vrfs_read) | **GET** /ipam/vrfs/{id}/ | 
[**ipam_vrfs_update**](IpamApi.md#ipam_vrfs_update) | **PUT** /ipam/vrfs/{id}/ | 


# **ipam_aggregates_create**
> Aggregate ipam_aggregates_create(data)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
data = aionetbox.WritableAggregate() # WritableAggregate | 

try:
    api_response = api_instance.ipam_aggregates_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_aggregates_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WritableAggregate**](WritableAggregate.md)|  | 

### Return type

[**Aggregate**](Aggregate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_aggregates_delete**
> ipam_aggregates_delete(id)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this aggregate.

try:
    api_instance.ipam_aggregates_delete(id)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_aggregates_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this aggregate. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_aggregates_list**
> InlineResponse20044 ipam_aggregates_list(family=family, date_added=date_added, id__in=id__in, q=q, prefix=prefix, rir_id=rir_id, rir=rir, tag=tag, limit=limit, offset=offset)



Call to super to allow for caching

### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
family = 'family_example' # str |  (optional)
date_added = 'date_added_example' # str |  (optional)
id__in = 'id__in_example' # str | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
prefix = 'prefix_example' # str |  (optional)
rir_id = 'rir_id_example' # str |  (optional)
rir = 'rir_example' # str |  (optional)
tag = 'tag_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.ipam_aggregates_list(family=family, date_added=date_added, id__in=id__in, q=q, prefix=prefix, rir_id=rir_id, rir=rir, tag=tag, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_aggregates_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **family** | **str**|  | [optional] 
 **date_added** | **str**|  | [optional] 
 **id__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **q** | **str**|  | [optional] 
 **prefix** | **str**|  | [optional] 
 **rir_id** | **str**|  | [optional] 
 **rir** | **str**|  | [optional] 
 **tag** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20044**](InlineResponse20044.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_aggregates_partial_update**
> Aggregate ipam_aggregates_partial_update(id, data)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this aggregate.
data = aionetbox.WritableAggregate() # WritableAggregate | 

try:
    api_response = api_instance.ipam_aggregates_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_aggregates_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this aggregate. | 
 **data** | [**WritableAggregate**](WritableAggregate.md)|  | 

### Return type

[**Aggregate**](Aggregate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_aggregates_read**
> Aggregate ipam_aggregates_read(id)



Call to super to allow for caching

### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this aggregate.

try:
    api_response = api_instance.ipam_aggregates_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_aggregates_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this aggregate. | 

### Return type

[**Aggregate**](Aggregate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_aggregates_update**
> Aggregate ipam_aggregates_update(id, data)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this aggregate.
data = aionetbox.WritableAggregate() # WritableAggregate | 

try:
    api_response = api_instance.ipam_aggregates_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_aggregates_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this aggregate. | 
 **data** | [**WritableAggregate**](WritableAggregate.md)|  | 

### Return type

[**Aggregate**](Aggregate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_choices_list**
> ipam_choices_list()





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))

try:
    api_instance.ipam_choices_list()
except ApiException as e:
    print("Exception when calling IpamApi->ipam_choices_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_choices_read**
> ipam_choices_read(id)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.ipam_choices_read(id)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_choices_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_ip_addresses_create**
> IPAddress ipam_ip_addresses_create(data)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
data = aionetbox.WritableIPAddress() # WritableIPAddress | 

try:
    api_response = api_instance.ipam_ip_addresses_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_ip_addresses_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WritableIPAddress**](WritableIPAddress.md)|  | 

### Return type

[**IPAddress**](IPAddress.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_ip_addresses_delete**
> ipam_ip_addresses_delete(id)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this IP address.

try:
    api_instance.ipam_ip_addresses_delete(id)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_ip_addresses_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this IP address. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_ip_addresses_list**
> InlineResponse20045 ipam_ip_addresses_list(family=family, dns_name=dns_name, tenant_group_id=tenant_group_id, tenant_group=tenant_group, tenant_id=tenant_id, tenant=tenant, id__in=id__in, q=q, parent=parent, address=address, mask_length=mask_length, vrf_id=vrf_id, vrf=vrf, device=device, device_id=device_id, virtual_machine_id=virtual_machine_id, virtual_machine=virtual_machine, interface=interface, interface_id=interface_id, status=status, role=role, tag=tag, limit=limit, offset=offset)



Call to super to allow for caching

### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
family = 'family_example' # str |  (optional)
dns_name = 'dns_name_example' # str |  (optional)
tenant_group_id = 'tenant_group_id_example' # str |  (optional)
tenant_group = 'tenant_group_example' # str |  (optional)
tenant_id = 'tenant_id_example' # str |  (optional)
tenant = 'tenant_example' # str |  (optional)
id__in = 'id__in_example' # str | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
parent = 'parent_example' # str |  (optional)
address = 'address_example' # str |  (optional)
mask_length = 8.14 # float |  (optional)
vrf_id = 'vrf_id_example' # str |  (optional)
vrf = 'vrf_example' # str |  (optional)
device = 'device_example' # str |  (optional)
device_id = 8.14 # float |  (optional)
virtual_machine_id = 'virtual_machine_id_example' # str |  (optional)
virtual_machine = 'virtual_machine_example' # str |  (optional)
interface = 'interface_example' # str |  (optional)
interface_id = 'interface_id_example' # str |  (optional)
status = 'status_example' # str |  (optional)
role = 'role_example' # str |  (optional)
tag = 'tag_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.ipam_ip_addresses_list(family=family, dns_name=dns_name, tenant_group_id=tenant_group_id, tenant_group=tenant_group, tenant_id=tenant_id, tenant=tenant, id__in=id__in, q=q, parent=parent, address=address, mask_length=mask_length, vrf_id=vrf_id, vrf=vrf, device=device, device_id=device_id, virtual_machine_id=virtual_machine_id, virtual_machine=virtual_machine, interface=interface, interface_id=interface_id, status=status, role=role, tag=tag, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_ip_addresses_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **family** | **str**|  | [optional] 
 **dns_name** | **str**|  | [optional] 
 **tenant_group_id** | **str**|  | [optional] 
 **tenant_group** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **tenant** | **str**|  | [optional] 
 **id__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **q** | **str**|  | [optional] 
 **parent** | **str**|  | [optional] 
 **address** | **str**|  | [optional] 
 **mask_length** | **float**|  | [optional] 
 **vrf_id** | **str**|  | [optional] 
 **vrf** | **str**|  | [optional] 
 **device** | **str**|  | [optional] 
 **device_id** | **float**|  | [optional] 
 **virtual_machine_id** | **str**|  | [optional] 
 **virtual_machine** | **str**|  | [optional] 
 **interface** | **str**|  | [optional] 
 **interface_id** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **role** | **str**|  | [optional] 
 **tag** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20045**](InlineResponse20045.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_ip_addresses_partial_update**
> IPAddress ipam_ip_addresses_partial_update(id, data)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this IP address.
data = aionetbox.WritableIPAddress() # WritableIPAddress | 

try:
    api_response = api_instance.ipam_ip_addresses_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_ip_addresses_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this IP address. | 
 **data** | [**WritableIPAddress**](WritableIPAddress.md)|  | 

### Return type

[**IPAddress**](IPAddress.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_ip_addresses_read**
> IPAddress ipam_ip_addresses_read(id)



Call to super to allow for caching

### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this IP address.

try:
    api_response = api_instance.ipam_ip_addresses_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_ip_addresses_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this IP address. | 

### Return type

[**IPAddress**](IPAddress.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_ip_addresses_update**
> IPAddress ipam_ip_addresses_update(id, data)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this IP address.
data = aionetbox.WritableIPAddress() # WritableIPAddress | 

try:
    api_response = api_instance.ipam_ip_addresses_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_ip_addresses_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this IP address. | 
 **data** | [**WritableIPAddress**](WritableIPAddress.md)|  | 

### Return type

[**IPAddress**](IPAddress.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_prefixes_available_ips_create**
> Prefix ipam_prefixes_available_ips_create(id, data)



A convenience method for returning available IP addresses within a prefix. By default, the number of IPs returned will be equivalent to PAGINATE_COUNT. An arbitrary limit (up to MAX_PAGE_SIZE, if set) may be passed, however results will not be paginated.

### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this prefix.
data = aionetbox.WritablePrefix() # WritablePrefix | 

try:
    api_response = api_instance.ipam_prefixes_available_ips_create(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_prefixes_available_ips_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this prefix. | 
 **data** | [**WritablePrefix**](WritablePrefix.md)|  | 

### Return type

[**Prefix**](Prefix.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_prefixes_available_ips_read**
> Prefix ipam_prefixes_available_ips_read(id)



A convenience method for returning available IP addresses within a prefix. By default, the number of IPs returned will be equivalent to PAGINATE_COUNT. An arbitrary limit (up to MAX_PAGE_SIZE, if set) may be passed, however results will not be paginated.

### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this prefix.

try:
    api_response = api_instance.ipam_prefixes_available_ips_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_prefixes_available_ips_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this prefix. | 

### Return type

[**Prefix**](Prefix.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_prefixes_available_prefixes_create**
> Prefix ipam_prefixes_available_prefixes_create(id, data)



A convenience method for returning available child prefixes within a parent.

### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this prefix.
data = aionetbox.WritablePrefix() # WritablePrefix | 

try:
    api_response = api_instance.ipam_prefixes_available_prefixes_create(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_prefixes_available_prefixes_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this prefix. | 
 **data** | [**WritablePrefix**](WritablePrefix.md)|  | 

### Return type

[**Prefix**](Prefix.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_prefixes_available_prefixes_read**
> Prefix ipam_prefixes_available_prefixes_read(id)



A convenience method for returning available child prefixes within a parent.

### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this prefix.

try:
    api_response = api_instance.ipam_prefixes_available_prefixes_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_prefixes_available_prefixes_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this prefix. | 

### Return type

[**Prefix**](Prefix.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_prefixes_create**
> Prefix ipam_prefixes_create(data)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
data = aionetbox.WritablePrefix() # WritablePrefix | 

try:
    api_response = api_instance.ipam_prefixes_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_prefixes_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WritablePrefix**](WritablePrefix.md)|  | 

### Return type

[**Prefix**](Prefix.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_prefixes_delete**
> ipam_prefixes_delete(id)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this prefix.

try:
    api_instance.ipam_prefixes_delete(id)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_prefixes_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this prefix. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_prefixes_list**
> InlineResponse20046 ipam_prefixes_list(family=family, is_pool=is_pool, tenant_group_id=tenant_group_id, tenant_group=tenant_group, tenant_id=tenant_id, tenant=tenant, id__in=id__in, q=q, prefix=prefix, within=within, within_include=within_include, contains=contains, mask_length=mask_length, vrf_id=vrf_id, vrf=vrf, site_id=site_id, site=site, vlan_id=vlan_id, vlan_vid=vlan_vid, role_id=role_id, role=role, status=status, tag=tag, limit=limit, offset=offset)



Call to super to allow for caching

### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
family = 'family_example' # str |  (optional)
is_pool = 'is_pool_example' # str |  (optional)
tenant_group_id = 'tenant_group_id_example' # str |  (optional)
tenant_group = 'tenant_group_example' # str |  (optional)
tenant_id = 'tenant_id_example' # str |  (optional)
tenant = 'tenant_example' # str |  (optional)
id__in = 'id__in_example' # str | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
prefix = 'prefix_example' # str |  (optional)
within = 'within_example' # str |  (optional)
within_include = 'within_include_example' # str |  (optional)
contains = 'contains_example' # str |  (optional)
mask_length = 8.14 # float |  (optional)
vrf_id = 'vrf_id_example' # str |  (optional)
vrf = 'vrf_example' # str |  (optional)
site_id = 'site_id_example' # str |  (optional)
site = 'site_example' # str |  (optional)
vlan_id = 'vlan_id_example' # str |  (optional)
vlan_vid = 8.14 # float |  (optional)
role_id = 'role_id_example' # str |  (optional)
role = 'role_example' # str |  (optional)
status = 'status_example' # str |  (optional)
tag = 'tag_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.ipam_prefixes_list(family=family, is_pool=is_pool, tenant_group_id=tenant_group_id, tenant_group=tenant_group, tenant_id=tenant_id, tenant=tenant, id__in=id__in, q=q, prefix=prefix, within=within, within_include=within_include, contains=contains, mask_length=mask_length, vrf_id=vrf_id, vrf=vrf, site_id=site_id, site=site, vlan_id=vlan_id, vlan_vid=vlan_vid, role_id=role_id, role=role, status=status, tag=tag, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_prefixes_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **family** | **str**|  | [optional] 
 **is_pool** | **str**|  | [optional] 
 **tenant_group_id** | **str**|  | [optional] 
 **tenant_group** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **tenant** | **str**|  | [optional] 
 **id__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **q** | **str**|  | [optional] 
 **prefix** | **str**|  | [optional] 
 **within** | **str**|  | [optional] 
 **within_include** | **str**|  | [optional] 
 **contains** | **str**|  | [optional] 
 **mask_length** | **float**|  | [optional] 
 **vrf_id** | **str**|  | [optional] 
 **vrf** | **str**|  | [optional] 
 **site_id** | **str**|  | [optional] 
 **site** | **str**|  | [optional] 
 **vlan_id** | **str**|  | [optional] 
 **vlan_vid** | **float**|  | [optional] 
 **role_id** | **str**|  | [optional] 
 **role** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **tag** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20046**](InlineResponse20046.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_prefixes_partial_update**
> Prefix ipam_prefixes_partial_update(id, data)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this prefix.
data = aionetbox.WritablePrefix() # WritablePrefix | 

try:
    api_response = api_instance.ipam_prefixes_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_prefixes_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this prefix. | 
 **data** | [**WritablePrefix**](WritablePrefix.md)|  | 

### Return type

[**Prefix**](Prefix.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_prefixes_read**
> Prefix ipam_prefixes_read(id)



Call to super to allow for caching

### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this prefix.

try:
    api_response = api_instance.ipam_prefixes_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_prefixes_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this prefix. | 

### Return type

[**Prefix**](Prefix.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_prefixes_update**
> Prefix ipam_prefixes_update(id, data)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this prefix.
data = aionetbox.WritablePrefix() # WritablePrefix | 

try:
    api_response = api_instance.ipam_prefixes_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_prefixes_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this prefix. | 
 **data** | [**WritablePrefix**](WritablePrefix.md)|  | 

### Return type

[**Prefix**](Prefix.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_rirs_create**
> RIR ipam_rirs_create(data)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
data = aionetbox.RIR() # RIR | 

try:
    api_response = api_instance.ipam_rirs_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_rirs_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**RIR**](RIR.md)|  | 

### Return type

[**RIR**](RIR.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_rirs_delete**
> ipam_rirs_delete(id)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this RIR.

try:
    api_instance.ipam_rirs_delete(id)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_rirs_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this RIR. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_rirs_list**
> InlineResponse20047 ipam_rirs_list(name=name, slug=slug, is_private=is_private, q=q, id__in=id__in, limit=limit, offset=offset)



Call to super to allow for caching

### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
name = 'name_example' # str |  (optional)
slug = 'slug_example' # str |  (optional)
is_private = 'is_private_example' # str |  (optional)
q = 'q_example' # str |  (optional)
id__in = 'id__in_example' # str | Multiple values may be separated by commas. (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.ipam_rirs_list(name=name, slug=slug, is_private=is_private, q=q, id__in=id__in, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_rirs_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **slug** | **str**|  | [optional] 
 **is_private** | **str**|  | [optional] 
 **q** | **str**|  | [optional] 
 **id__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20047**](InlineResponse20047.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_rirs_partial_update**
> RIR ipam_rirs_partial_update(id, data)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this RIR.
data = aionetbox.RIR() # RIR | 

try:
    api_response = api_instance.ipam_rirs_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_rirs_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this RIR. | 
 **data** | [**RIR**](RIR.md)|  | 

### Return type

[**RIR**](RIR.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_rirs_read**
> RIR ipam_rirs_read(id)



Call to super to allow for caching

### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this RIR.

try:
    api_response = api_instance.ipam_rirs_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_rirs_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this RIR. | 

### Return type

[**RIR**](RIR.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_rirs_update**
> RIR ipam_rirs_update(id, data)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this RIR.
data = aionetbox.RIR() # RIR | 

try:
    api_response = api_instance.ipam_rirs_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_rirs_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this RIR. | 
 **data** | [**RIR**](RIR.md)|  | 

### Return type

[**RIR**](RIR.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_roles_create**
> Role ipam_roles_create(data)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
data = aionetbox.Role() # Role | 

try:
    api_response = api_instance.ipam_roles_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_roles_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Role**](Role.md)|  | 

### Return type

[**Role**](Role.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_roles_delete**
> ipam_roles_delete(id)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this role.

try:
    api_instance.ipam_roles_delete(id)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_roles_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this role. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_roles_list**
> InlineResponse20048 ipam_roles_list(id=id, name=name, slug=slug, q=q, limit=limit, offset=offset)



Call to super to allow for caching

### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
slug = 'slug_example' # str |  (optional)
q = 'q_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.ipam_roles_list(id=id, name=name, slug=slug, q=q, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_roles_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **slug** | **str**|  | [optional] 
 **q** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20048**](InlineResponse20048.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_roles_partial_update**
> Role ipam_roles_partial_update(id, data)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this role.
data = aionetbox.Role() # Role | 

try:
    api_response = api_instance.ipam_roles_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_roles_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this role. | 
 **data** | [**Role**](Role.md)|  | 

### Return type

[**Role**](Role.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_roles_read**
> Role ipam_roles_read(id)



Call to super to allow for caching

### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this role.

try:
    api_response = api_instance.ipam_roles_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_roles_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this role. | 

### Return type

[**Role**](Role.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_roles_update**
> Role ipam_roles_update(id, data)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this role.
data = aionetbox.Role() # Role | 

try:
    api_response = api_instance.ipam_roles_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_roles_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this role. | 
 **data** | [**Role**](Role.md)|  | 

### Return type

[**Role**](Role.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_services_create**
> Service ipam_services_create(data)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
data = aionetbox.WritableService() # WritableService | 

try:
    api_response = api_instance.ipam_services_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_services_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WritableService**](WritableService.md)|  | 

### Return type

[**Service**](Service.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_services_delete**
> ipam_services_delete(id)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this service.

try:
    api_instance.ipam_services_delete(id)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_services_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this service. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_services_list**
> InlineResponse20049 ipam_services_list(id=id, name=name, protocol=protocol, port=port, q=q, device_id=device_id, device=device, virtual_machine_id=virtual_machine_id, virtual_machine=virtual_machine, tag=tag, limit=limit, offset=offset)



Call to super to allow for caching

### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
protocol = 'protocol_example' # str |  (optional)
port = 'port_example' # str |  (optional)
q = 'q_example' # str |  (optional)
device_id = 'device_id_example' # str |  (optional)
device = 'device_example' # str |  (optional)
virtual_machine_id = 'virtual_machine_id_example' # str |  (optional)
virtual_machine = 'virtual_machine_example' # str |  (optional)
tag = 'tag_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.ipam_services_list(id=id, name=name, protocol=protocol, port=port, q=q, device_id=device_id, device=device, virtual_machine_id=virtual_machine_id, virtual_machine=virtual_machine, tag=tag, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_services_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **protocol** | **str**|  | [optional] 
 **port** | **str**|  | [optional] 
 **q** | **str**|  | [optional] 
 **device_id** | **str**|  | [optional] 
 **device** | **str**|  | [optional] 
 **virtual_machine_id** | **str**|  | [optional] 
 **virtual_machine** | **str**|  | [optional] 
 **tag** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20049**](InlineResponse20049.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_services_partial_update**
> Service ipam_services_partial_update(id, data)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this service.
data = aionetbox.WritableService() # WritableService | 

try:
    api_response = api_instance.ipam_services_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_services_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this service. | 
 **data** | [**WritableService**](WritableService.md)|  | 

### Return type

[**Service**](Service.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_services_read**
> Service ipam_services_read(id)



Call to super to allow for caching

### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this service.

try:
    api_response = api_instance.ipam_services_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_services_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this service. | 

### Return type

[**Service**](Service.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_services_update**
> Service ipam_services_update(id, data)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this service.
data = aionetbox.WritableService() # WritableService | 

try:
    api_response = api_instance.ipam_services_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_services_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this service. | 
 **data** | [**WritableService**](WritableService.md)|  | 

### Return type

[**Service**](Service.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_vlan_groups_create**
> VLANGroup ipam_vlan_groups_create(data)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
data = aionetbox.WritableVLANGroup() # WritableVLANGroup | 

try:
    api_response = api_instance.ipam_vlan_groups_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_vlan_groups_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WritableVLANGroup**](WritableVLANGroup.md)|  | 

### Return type

[**VLANGroup**](VLANGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_vlan_groups_delete**
> ipam_vlan_groups_delete(id)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this VLAN group.

try:
    api_instance.ipam_vlan_groups_delete(id)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_vlan_groups_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this VLAN group. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_vlan_groups_list**
> InlineResponse20050 ipam_vlan_groups_list(id=id, name=name, slug=slug, q=q, site_id=site_id, site=site, limit=limit, offset=offset)



Call to super to allow for caching

### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
slug = 'slug_example' # str |  (optional)
q = 'q_example' # str |  (optional)
site_id = 'site_id_example' # str |  (optional)
site = 'site_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.ipam_vlan_groups_list(id=id, name=name, slug=slug, q=q, site_id=site_id, site=site, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_vlan_groups_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **slug** | **str**|  | [optional] 
 **q** | **str**|  | [optional] 
 **site_id** | **str**|  | [optional] 
 **site** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20050**](InlineResponse20050.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_vlan_groups_partial_update**
> VLANGroup ipam_vlan_groups_partial_update(id, data)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this VLAN group.
data = aionetbox.WritableVLANGroup() # WritableVLANGroup | 

try:
    api_response = api_instance.ipam_vlan_groups_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_vlan_groups_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this VLAN group. | 
 **data** | [**WritableVLANGroup**](WritableVLANGroup.md)|  | 

### Return type

[**VLANGroup**](VLANGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_vlan_groups_read**
> VLANGroup ipam_vlan_groups_read(id)



Call to super to allow for caching

### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this VLAN group.

try:
    api_response = api_instance.ipam_vlan_groups_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_vlan_groups_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this VLAN group. | 

### Return type

[**VLANGroup**](VLANGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_vlan_groups_update**
> VLANGroup ipam_vlan_groups_update(id, data)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this VLAN group.
data = aionetbox.WritableVLANGroup() # WritableVLANGroup | 

try:
    api_response = api_instance.ipam_vlan_groups_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_vlan_groups_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this VLAN group. | 
 **data** | [**WritableVLANGroup**](WritableVLANGroup.md)|  | 

### Return type

[**VLANGroup**](VLANGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_vlans_create**
> VLAN ipam_vlans_create(data)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
data = aionetbox.WritableVLAN() # WritableVLAN | 

try:
    api_response = api_instance.ipam_vlans_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_vlans_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WritableVLAN**](WritableVLAN.md)|  | 

### Return type

[**VLAN**](VLAN.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_vlans_delete**
> ipam_vlans_delete(id)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this VLAN.

try:
    api_instance.ipam_vlans_delete(id)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_vlans_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this VLAN. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_vlans_list**
> InlineResponse20051 ipam_vlans_list(vid=vid, name=name, tenant_group_id=tenant_group_id, tenant_group=tenant_group, tenant_id=tenant_id, tenant=tenant, id__in=id__in, q=q, site_id=site_id, site=site, group_id=group_id, group=group, role_id=role_id, role=role, status=status, tag=tag, limit=limit, offset=offset)



Call to super to allow for caching

### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
vid = 'vid_example' # str |  (optional)
name = 'name_example' # str |  (optional)
tenant_group_id = 'tenant_group_id_example' # str |  (optional)
tenant_group = 'tenant_group_example' # str |  (optional)
tenant_id = 'tenant_id_example' # str |  (optional)
tenant = 'tenant_example' # str |  (optional)
id__in = 'id__in_example' # str | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
site_id = 'site_id_example' # str |  (optional)
site = 'site_example' # str |  (optional)
group_id = 'group_id_example' # str |  (optional)
group = 'group_example' # str |  (optional)
role_id = 'role_id_example' # str |  (optional)
role = 'role_example' # str |  (optional)
status = 'status_example' # str |  (optional)
tag = 'tag_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.ipam_vlans_list(vid=vid, name=name, tenant_group_id=tenant_group_id, tenant_group=tenant_group, tenant_id=tenant_id, tenant=tenant, id__in=id__in, q=q, site_id=site_id, site=site, group_id=group_id, group=group, role_id=role_id, role=role, status=status, tag=tag, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_vlans_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vid** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **tenant_group_id** | **str**|  | [optional] 
 **tenant_group** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **tenant** | **str**|  | [optional] 
 **id__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **q** | **str**|  | [optional] 
 **site_id** | **str**|  | [optional] 
 **site** | **str**|  | [optional] 
 **group_id** | **str**|  | [optional] 
 **group** | **str**|  | [optional] 
 **role_id** | **str**|  | [optional] 
 **role** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **tag** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20051**](InlineResponse20051.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_vlans_partial_update**
> VLAN ipam_vlans_partial_update(id, data)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this VLAN.
data = aionetbox.WritableVLAN() # WritableVLAN | 

try:
    api_response = api_instance.ipam_vlans_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_vlans_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this VLAN. | 
 **data** | [**WritableVLAN**](WritableVLAN.md)|  | 

### Return type

[**VLAN**](VLAN.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_vlans_read**
> VLAN ipam_vlans_read(id)



Call to super to allow for caching

### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this VLAN.

try:
    api_response = api_instance.ipam_vlans_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_vlans_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this VLAN. | 

### Return type

[**VLAN**](VLAN.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_vlans_update**
> VLAN ipam_vlans_update(id, data)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this VLAN.
data = aionetbox.WritableVLAN() # WritableVLAN | 

try:
    api_response = api_instance.ipam_vlans_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_vlans_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this VLAN. | 
 **data** | [**WritableVLAN**](WritableVLAN.md)|  | 

### Return type

[**VLAN**](VLAN.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_vrfs_create**
> VRF ipam_vrfs_create(data)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
data = aionetbox.WritableVRF() # WritableVRF | 

try:
    api_response = api_instance.ipam_vrfs_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_vrfs_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WritableVRF**](WritableVRF.md)|  | 

### Return type

[**VRF**](VRF.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_vrfs_delete**
> ipam_vrfs_delete(id)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this VRF.

try:
    api_instance.ipam_vrfs_delete(id)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_vrfs_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this VRF. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_vrfs_list**
> InlineResponse20052 ipam_vrfs_list(name=name, rd=rd, enforce_unique=enforce_unique, tenant_group_id=tenant_group_id, tenant_group=tenant_group, tenant_id=tenant_id, tenant=tenant, id__in=id__in, q=q, tag=tag, limit=limit, offset=offset)



Call to super to allow for caching

### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
name = 'name_example' # str |  (optional)
rd = 'rd_example' # str |  (optional)
enforce_unique = 'enforce_unique_example' # str |  (optional)
tenant_group_id = 'tenant_group_id_example' # str |  (optional)
tenant_group = 'tenant_group_example' # str |  (optional)
tenant_id = 'tenant_id_example' # str |  (optional)
tenant = 'tenant_example' # str |  (optional)
id__in = 'id__in_example' # str | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
tag = 'tag_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.ipam_vrfs_list(name=name, rd=rd, enforce_unique=enforce_unique, tenant_group_id=tenant_group_id, tenant_group=tenant_group, tenant_id=tenant_id, tenant=tenant, id__in=id__in, q=q, tag=tag, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_vrfs_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **rd** | **str**|  | [optional] 
 **enforce_unique** | **str**|  | [optional] 
 **tenant_group_id** | **str**|  | [optional] 
 **tenant_group** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **tenant** | **str**|  | [optional] 
 **id__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **q** | **str**|  | [optional] 
 **tag** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20052**](InlineResponse20052.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_vrfs_partial_update**
> VRF ipam_vrfs_partial_update(id, data)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this VRF.
data = aionetbox.WritableVRF() # WritableVRF | 

try:
    api_response = api_instance.ipam_vrfs_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_vrfs_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this VRF. | 
 **data** | [**WritableVRF**](WritableVRF.md)|  | 

### Return type

[**VRF**](VRF.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_vrfs_read**
> VRF ipam_vrfs_read(id)



Call to super to allow for caching

### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this VRF.

try:
    api_response = api_instance.ipam_vrfs_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_vrfs_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this VRF. | 

### Return type

[**VRF**](VRF.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ipam_vrfs_update**
> VRF ipam_vrfs_update(id, data)





### Example
```python
from __future__ import print_function
import time
import aionetbox
from aionetbox.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = aionetbox.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = aionetbox.IpamApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this VRF.
data = aionetbox.WritableVRF() # WritableVRF | 

try:
    api_response = api_instance.ipam_vrfs_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IpamApi->ipam_vrfs_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this VRF. | 
 **data** | [**WritableVRF**](WritableVRF.md)|  | 

### Return type

[**VRF**](VRF.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

