# aionetbox.VaporApi

All URIs are relative to *http://ceppi.ngrok.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vapor_customers_create**](VaporApi.md#vapor_customers_create) | **POST** /vapor/customers/ | 
[**vapor_customers_delete**](VaporApi.md#vapor_customers_delete) | **DELETE** /vapor/customers/{id}/ | 
[**vapor_customers_list**](VaporApi.md#vapor_customers_list) | **GET** /vapor/customers/ | 
[**vapor_customers_partial_update**](VaporApi.md#vapor_customers_partial_update) | **PATCH** /vapor/customers/{id}/ | 
[**vapor_customers_read**](VaporApi.md#vapor_customers_read) | **GET** /vapor/customers/{id}/ | 
[**vapor_customers_update**](VaporApi.md#vapor_customers_update) | **PUT** /vapor/customers/{id}/ | 
[**vapor_interfaces_create**](VaporApi.md#vapor_interfaces_create) | **POST** /vapor/interfaces/ | 
[**vapor_interfaces_delete**](VaporApi.md#vapor_interfaces_delete) | **DELETE** /vapor/interfaces/{id}/ | 
[**vapor_interfaces_graphs**](VaporApi.md#vapor_interfaces_graphs) | **GET** /vapor/interfaces/{id}/graphs/ | 
[**vapor_interfaces_list**](VaporApi.md#vapor_interfaces_list) | **GET** /vapor/interfaces/ | 
[**vapor_interfaces_partial_update**](VaporApi.md#vapor_interfaces_partial_update) | **PATCH** /vapor/interfaces/{id}/ | 
[**vapor_interfaces_read**](VaporApi.md#vapor_interfaces_read) | **GET** /vapor/interfaces/{id}/ | 
[**vapor_interfaces_trace**](VaporApi.md#vapor_interfaces_trace) | **GET** /vapor/interfaces/{id}/trace/ | 
[**vapor_interfaces_update**](VaporApi.md#vapor_interfaces_update) | **PUT** /vapor/interfaces/{id}/ | 


# **vapor_customers_create**
> Customer vapor_customers_create(data)





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
api_instance = aionetbox.VaporApi(aionetbox.ApiClient(configuration))
data = aionetbox.WritableCustomer() # WritableCustomer | 

try:
    api_response = api_instance.vapor_customers_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VaporApi->vapor_customers_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WritableCustomer**](WritableCustomer.md)|  | 

### Return type

[**Customer**](Customer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vapor_customers_delete**
> vapor_customers_delete(id)





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
api_instance = aionetbox.VaporApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tenant.

try:
    api_instance.vapor_customers_delete(id)
except ApiException as e:
    print("Exception when calling VaporApi->vapor_customers_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tenant. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vapor_customers_list**
> InlineResponse20057 vapor_customers_list(name=name, slug=slug, id__in=id__in, q=q, group_id=group_id, group=group, tag=tag, device_role=device_role, limit=limit, offset=offset)



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
api_instance = aionetbox.VaporApi(aionetbox.ApiClient(configuration))
name = 'name_example' # str |  (optional)
slug = 'slug_example' # str |  (optional)
id__in = 'id__in_example' # str | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
group_id = 'group_id_example' # str |  (optional)
group = 'group_example' # str |  (optional)
tag = 'tag_example' # str |  (optional)
device_role = 'device_role_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.vapor_customers_list(name=name, slug=slug, id__in=id__in, q=q, group_id=group_id, group=group, tag=tag, device_role=device_role, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VaporApi->vapor_customers_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **slug** | **str**|  | [optional] 
 **id__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **q** | **str**|  | [optional] 
 **group_id** | **str**|  | [optional] 
 **group** | **str**|  | [optional] 
 **tag** | **str**|  | [optional] 
 **device_role** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20057**](InlineResponse20057.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vapor_customers_partial_update**
> Customer vapor_customers_partial_update(id, data)





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
api_instance = aionetbox.VaporApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tenant.
data = aionetbox.WritableCustomer() # WritableCustomer | 

try:
    api_response = api_instance.vapor_customers_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VaporApi->vapor_customers_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tenant. | 
 **data** | [**WritableCustomer**](WritableCustomer.md)|  | 

### Return type

[**Customer**](Customer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vapor_customers_read**
> Customer vapor_customers_read(id)



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
api_instance = aionetbox.VaporApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tenant.

try:
    api_response = api_instance.vapor_customers_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VaporApi->vapor_customers_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tenant. | 

### Return type

[**Customer**](Customer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vapor_customers_update**
> Customer vapor_customers_update(id, data)





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
api_instance = aionetbox.VaporApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tenant.
data = aionetbox.WritableCustomer() # WritableCustomer | 

try:
    api_response = api_instance.vapor_customers_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VaporApi->vapor_customers_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tenant. | 
 **data** | [**WritableCustomer**](WritableCustomer.md)|  | 

### Return type

[**Customer**](Customer.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vapor_interfaces_create**
> Interface vapor_interfaces_create(data)





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
api_instance = aionetbox.VaporApi(aionetbox.ApiClient(configuration))
data = aionetbox.WritableInterface() # WritableInterface | 

try:
    api_response = api_instance.vapor_interfaces_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VaporApi->vapor_interfaces_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WritableInterface**](WritableInterface.md)|  | 

### Return type

[**Interface**](Interface.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vapor_interfaces_delete**
> vapor_interfaces_delete(id)





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
api_instance = aionetbox.VaporApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this interface.

try:
    api_instance.vapor_interfaces_delete(id)
except ApiException as e:
    print("Exception when calling VaporApi->vapor_interfaces_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this interface. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vapor_interfaces_graphs**
> Interface vapor_interfaces_graphs(id)



A convenience method for rendering graphs for a particular interface.

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
api_instance = aionetbox.VaporApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this interface.

try:
    api_response = api_instance.vapor_interfaces_graphs(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VaporApi->vapor_interfaces_graphs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this interface. | 

### Return type

[**Interface**](Interface.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vapor_interfaces_list**
> InlineResponse20058 vapor_interfaces_list(id=id, name=name, connection_status=connection_status, type=type, enabled=enabled, mtu=mtu, mgmt_only=mgmt_only, mode=mode, description=description, q=q, device=device, device_id=device_id, cabled=cabled, kind=kind, lag_id=lag_id, mac_address=mac_address, tag=tag, vlan_id=vlan_id, vlan=vlan, customer=customer, limit=limit, offset=offset)



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
api_instance = aionetbox.VaporApi(aionetbox.ApiClient(configuration))
id = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
connection_status = 'connection_status_example' # str |  (optional)
type = 'type_example' # str |  (optional)
enabled = 'enabled_example' # str |  (optional)
mtu = 'mtu_example' # str |  (optional)
mgmt_only = 'mgmt_only_example' # str |  (optional)
mode = 'mode_example' # str |  (optional)
description = 'description_example' # str |  (optional)
q = 'q_example' # str |  (optional)
device = 'device_example' # str |  (optional)
device_id = 'device_id_example' # str |  (optional)
cabled = 'cabled_example' # str |  (optional)
kind = 'kind_example' # str |  (optional)
lag_id = 'lag_id_example' # str |  (optional)
mac_address = 'mac_address_example' # str |  (optional)
tag = 'tag_example' # str |  (optional)
vlan_id = 'vlan_id_example' # str |  (optional)
vlan = 'vlan_example' # str |  (optional)
customer = 'customer_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.vapor_interfaces_list(id=id, name=name, connection_status=connection_status, type=type, enabled=enabled, mtu=mtu, mgmt_only=mgmt_only, mode=mode, description=description, q=q, device=device, device_id=device_id, cabled=cabled, kind=kind, lag_id=lag_id, mac_address=mac_address, tag=tag, vlan_id=vlan_id, vlan=vlan, customer=customer, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VaporApi->vapor_interfaces_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **connection_status** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **enabled** | **str**|  | [optional] 
 **mtu** | **str**|  | [optional] 
 **mgmt_only** | **str**|  | [optional] 
 **mode** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **q** | **str**|  | [optional] 
 **device** | **str**|  | [optional] 
 **device_id** | **str**|  | [optional] 
 **cabled** | **str**|  | [optional] 
 **kind** | **str**|  | [optional] 
 **lag_id** | **str**|  | [optional] 
 **mac_address** | **str**|  | [optional] 
 **tag** | **str**|  | [optional] 
 **vlan_id** | **str**|  | [optional] 
 **vlan** | **str**|  | [optional] 
 **customer** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20058**](InlineResponse20058.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vapor_interfaces_partial_update**
> Interface vapor_interfaces_partial_update(id, data)





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
api_instance = aionetbox.VaporApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this interface.
data = aionetbox.WritableInterface() # WritableInterface | 

try:
    api_response = api_instance.vapor_interfaces_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VaporApi->vapor_interfaces_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this interface. | 
 **data** | [**WritableInterface**](WritableInterface.md)|  | 

### Return type

[**Interface**](Interface.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vapor_interfaces_read**
> Interface vapor_interfaces_read(id)



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
api_instance = aionetbox.VaporApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this interface.

try:
    api_response = api_instance.vapor_interfaces_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VaporApi->vapor_interfaces_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this interface. | 

### Return type

[**Interface**](Interface.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vapor_interfaces_trace**
> Interface vapor_interfaces_trace(id)



Trace a complete cable path and return each segment as a three-tuple of (termination, cable, termination).

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
api_instance = aionetbox.VaporApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this interface.

try:
    api_response = api_instance.vapor_interfaces_trace(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VaporApi->vapor_interfaces_trace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this interface. | 

### Return type

[**Interface**](Interface.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vapor_interfaces_update**
> Interface vapor_interfaces_update(id, data)





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
api_instance = aionetbox.VaporApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this interface.
data = aionetbox.WritableInterface() # WritableInterface | 

try:
    api_response = api_instance.vapor_interfaces_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VaporApi->vapor_interfaces_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this interface. | 
 **data** | [**WritableInterface**](WritableInterface.md)|  | 

### Return type

[**Interface**](Interface.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

