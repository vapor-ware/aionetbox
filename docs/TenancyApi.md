# aionetbox.TenancyApi

All URIs are relative to *http://ceppi.ngrok.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tenancy_choices_list**](TenancyApi.md#tenancy_choices_list) | **GET** /tenancy/_choices/ | 
[**tenancy_choices_read**](TenancyApi.md#tenancy_choices_read) | **GET** /tenancy/_choices/{id}/ | 
[**tenancy_tenant_groups_create**](TenancyApi.md#tenancy_tenant_groups_create) | **POST** /tenancy/tenant-groups/ | 
[**tenancy_tenant_groups_delete**](TenancyApi.md#tenancy_tenant_groups_delete) | **DELETE** /tenancy/tenant-groups/{id}/ | 
[**tenancy_tenant_groups_list**](TenancyApi.md#tenancy_tenant_groups_list) | **GET** /tenancy/tenant-groups/ | 
[**tenancy_tenant_groups_partial_update**](TenancyApi.md#tenancy_tenant_groups_partial_update) | **PATCH** /tenancy/tenant-groups/{id}/ | 
[**tenancy_tenant_groups_read**](TenancyApi.md#tenancy_tenant_groups_read) | **GET** /tenancy/tenant-groups/{id}/ | 
[**tenancy_tenant_groups_update**](TenancyApi.md#tenancy_tenant_groups_update) | **PUT** /tenancy/tenant-groups/{id}/ | 
[**tenancy_tenants_create**](TenancyApi.md#tenancy_tenants_create) | **POST** /tenancy/tenants/ | 
[**tenancy_tenants_delete**](TenancyApi.md#tenancy_tenants_delete) | **DELETE** /tenancy/tenants/{id}/ | 
[**tenancy_tenants_list**](TenancyApi.md#tenancy_tenants_list) | **GET** /tenancy/tenants/ | 
[**tenancy_tenants_partial_update**](TenancyApi.md#tenancy_tenants_partial_update) | **PATCH** /tenancy/tenants/{id}/ | 
[**tenancy_tenants_read**](TenancyApi.md#tenancy_tenants_read) | **GET** /tenancy/tenants/{id}/ | 
[**tenancy_tenants_update**](TenancyApi.md#tenancy_tenants_update) | **PUT** /tenancy/tenants/{id}/ | 


# **tenancy_choices_list**
> tenancy_choices_list()





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
api_instance = aionetbox.TenancyApi(aionetbox.ApiClient(configuration))

try:
    api_instance.tenancy_choices_list()
except ApiException as e:
    print("Exception when calling TenancyApi->tenancy_choices_list: %s\n" % e)
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

# **tenancy_choices_read**
> tenancy_choices_read(id)





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
api_instance = aionetbox.TenancyApi(aionetbox.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.tenancy_choices_read(id)
except ApiException as e:
    print("Exception when calling TenancyApi->tenancy_choices_read: %s\n" % e)
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

# **tenancy_tenant_groups_create**
> TenantGroup tenancy_tenant_groups_create(data)





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
api_instance = aionetbox.TenancyApi(aionetbox.ApiClient(configuration))
data = aionetbox.TenantGroup() # TenantGroup | 

try:
    api_response = api_instance.tenancy_tenant_groups_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenancyApi->tenancy_tenant_groups_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TenantGroup**](TenantGroup.md)|  | 

### Return type

[**TenantGroup**](TenantGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenancy_tenant_groups_delete**
> tenancy_tenant_groups_delete(id)





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
api_instance = aionetbox.TenancyApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tenant group.

try:
    api_instance.tenancy_tenant_groups_delete(id)
except ApiException as e:
    print("Exception when calling TenancyApi->tenancy_tenant_groups_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tenant group. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenancy_tenant_groups_list**
> InlineResponse20055 tenancy_tenant_groups_list(id=id, name=name, slug=slug, q=q, limit=limit, offset=offset)



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
api_instance = aionetbox.TenancyApi(aionetbox.ApiClient(configuration))
id = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
slug = 'slug_example' # str |  (optional)
q = 'q_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.tenancy_tenant_groups_list(id=id, name=name, slug=slug, q=q, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenancyApi->tenancy_tenant_groups_list: %s\n" % e)
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

[**InlineResponse20055**](InlineResponse20055.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenancy_tenant_groups_partial_update**
> TenantGroup tenancy_tenant_groups_partial_update(id, data)





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
api_instance = aionetbox.TenancyApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tenant group.
data = aionetbox.TenantGroup() # TenantGroup | 

try:
    api_response = api_instance.tenancy_tenant_groups_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenancyApi->tenancy_tenant_groups_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tenant group. | 
 **data** | [**TenantGroup**](TenantGroup.md)|  | 

### Return type

[**TenantGroup**](TenantGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenancy_tenant_groups_read**
> TenantGroup tenancy_tenant_groups_read(id)



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
api_instance = aionetbox.TenancyApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tenant group.

try:
    api_response = api_instance.tenancy_tenant_groups_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenancyApi->tenancy_tenant_groups_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tenant group. | 

### Return type

[**TenantGroup**](TenantGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenancy_tenant_groups_update**
> TenantGroup tenancy_tenant_groups_update(id, data)





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
api_instance = aionetbox.TenancyApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tenant group.
data = aionetbox.TenantGroup() # TenantGroup | 

try:
    api_response = api_instance.tenancy_tenant_groups_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenancyApi->tenancy_tenant_groups_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tenant group. | 
 **data** | [**TenantGroup**](TenantGroup.md)|  | 

### Return type

[**TenantGroup**](TenantGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenancy_tenants_create**
> Tenant tenancy_tenants_create(data)





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
api_instance = aionetbox.TenancyApi(aionetbox.ApiClient(configuration))
data = aionetbox.WritableTenant() # WritableTenant | 

try:
    api_response = api_instance.tenancy_tenants_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenancyApi->tenancy_tenants_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WritableTenant**](WritableTenant.md)|  | 

### Return type

[**Tenant**](Tenant.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenancy_tenants_delete**
> tenancy_tenants_delete(id)





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
api_instance = aionetbox.TenancyApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tenant.

try:
    api_instance.tenancy_tenants_delete(id)
except ApiException as e:
    print("Exception when calling TenancyApi->tenancy_tenants_delete: %s\n" % e)
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

# **tenancy_tenants_list**
> InlineResponse20056 tenancy_tenants_list(name=name, slug=slug, id__in=id__in, q=q, group_id=group_id, group=group, tag=tag, limit=limit, offset=offset)



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
api_instance = aionetbox.TenancyApi(aionetbox.ApiClient(configuration))
name = 'name_example' # str |  (optional)
slug = 'slug_example' # str |  (optional)
id__in = 'id__in_example' # str | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
group_id = 'group_id_example' # str |  (optional)
group = 'group_example' # str |  (optional)
tag = 'tag_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.tenancy_tenants_list(name=name, slug=slug, id__in=id__in, q=q, group_id=group_id, group=group, tag=tag, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenancyApi->tenancy_tenants_list: %s\n" % e)
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
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20056**](InlineResponse20056.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenancy_tenants_partial_update**
> Tenant tenancy_tenants_partial_update(id, data)





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
api_instance = aionetbox.TenancyApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tenant.
data = aionetbox.WritableTenant() # WritableTenant | 

try:
    api_response = api_instance.tenancy_tenants_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenancyApi->tenancy_tenants_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tenant. | 
 **data** | [**WritableTenant**](WritableTenant.md)|  | 

### Return type

[**Tenant**](Tenant.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenancy_tenants_read**
> Tenant tenancy_tenants_read(id)



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
api_instance = aionetbox.TenancyApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tenant.

try:
    api_response = api_instance.tenancy_tenants_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenancyApi->tenancy_tenants_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tenant. | 

### Return type

[**Tenant**](Tenant.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tenancy_tenants_update**
> Tenant tenancy_tenants_update(id, data)





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
api_instance = aionetbox.TenancyApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tenant.
data = aionetbox.WritableTenant() # WritableTenant | 

try:
    api_response = api_instance.tenancy_tenants_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TenancyApi->tenancy_tenants_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tenant. | 
 **data** | [**WritableTenant**](WritableTenant.md)|  | 

### Return type

[**Tenant**](Tenant.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

