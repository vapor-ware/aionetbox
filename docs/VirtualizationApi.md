# aionetbox.VirtualizationApi

All URIs are relative to *http://ceppi.ngrok.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**virtualization_choices_list**](VirtualizationApi.md#virtualization_choices_list) | **GET** /virtualization/_choices/ | 
[**virtualization_choices_read**](VirtualizationApi.md#virtualization_choices_read) | **GET** /virtualization/_choices/{id}/ | 
[**virtualization_cluster_groups_create**](VirtualizationApi.md#virtualization_cluster_groups_create) | **POST** /virtualization/cluster-groups/ | 
[**virtualization_cluster_groups_delete**](VirtualizationApi.md#virtualization_cluster_groups_delete) | **DELETE** /virtualization/cluster-groups/{id}/ | 
[**virtualization_cluster_groups_list**](VirtualizationApi.md#virtualization_cluster_groups_list) | **GET** /virtualization/cluster-groups/ | 
[**virtualization_cluster_groups_partial_update**](VirtualizationApi.md#virtualization_cluster_groups_partial_update) | **PATCH** /virtualization/cluster-groups/{id}/ | 
[**virtualization_cluster_groups_read**](VirtualizationApi.md#virtualization_cluster_groups_read) | **GET** /virtualization/cluster-groups/{id}/ | 
[**virtualization_cluster_groups_update**](VirtualizationApi.md#virtualization_cluster_groups_update) | **PUT** /virtualization/cluster-groups/{id}/ | 
[**virtualization_cluster_types_create**](VirtualizationApi.md#virtualization_cluster_types_create) | **POST** /virtualization/cluster-types/ | 
[**virtualization_cluster_types_delete**](VirtualizationApi.md#virtualization_cluster_types_delete) | **DELETE** /virtualization/cluster-types/{id}/ | 
[**virtualization_cluster_types_list**](VirtualizationApi.md#virtualization_cluster_types_list) | **GET** /virtualization/cluster-types/ | 
[**virtualization_cluster_types_partial_update**](VirtualizationApi.md#virtualization_cluster_types_partial_update) | **PATCH** /virtualization/cluster-types/{id}/ | 
[**virtualization_cluster_types_read**](VirtualizationApi.md#virtualization_cluster_types_read) | **GET** /virtualization/cluster-types/{id}/ | 
[**virtualization_cluster_types_update**](VirtualizationApi.md#virtualization_cluster_types_update) | **PUT** /virtualization/cluster-types/{id}/ | 
[**virtualization_clusters_create**](VirtualizationApi.md#virtualization_clusters_create) | **POST** /virtualization/clusters/ | 
[**virtualization_clusters_delete**](VirtualizationApi.md#virtualization_clusters_delete) | **DELETE** /virtualization/clusters/{id}/ | 
[**virtualization_clusters_list**](VirtualizationApi.md#virtualization_clusters_list) | **GET** /virtualization/clusters/ | 
[**virtualization_clusters_partial_update**](VirtualizationApi.md#virtualization_clusters_partial_update) | **PATCH** /virtualization/clusters/{id}/ | 
[**virtualization_clusters_read**](VirtualizationApi.md#virtualization_clusters_read) | **GET** /virtualization/clusters/{id}/ | 
[**virtualization_clusters_update**](VirtualizationApi.md#virtualization_clusters_update) | **PUT** /virtualization/clusters/{id}/ | 
[**virtualization_interfaces_create**](VirtualizationApi.md#virtualization_interfaces_create) | **POST** /virtualization/interfaces/ | 
[**virtualization_interfaces_delete**](VirtualizationApi.md#virtualization_interfaces_delete) | **DELETE** /virtualization/interfaces/{id}/ | 
[**virtualization_interfaces_list**](VirtualizationApi.md#virtualization_interfaces_list) | **GET** /virtualization/interfaces/ | 
[**virtualization_interfaces_partial_update**](VirtualizationApi.md#virtualization_interfaces_partial_update) | **PATCH** /virtualization/interfaces/{id}/ | 
[**virtualization_interfaces_read**](VirtualizationApi.md#virtualization_interfaces_read) | **GET** /virtualization/interfaces/{id}/ | 
[**virtualization_interfaces_update**](VirtualizationApi.md#virtualization_interfaces_update) | **PUT** /virtualization/interfaces/{id}/ | 
[**virtualization_virtual_machines_create**](VirtualizationApi.md#virtualization_virtual_machines_create) | **POST** /virtualization/virtual-machines/ | 
[**virtualization_virtual_machines_delete**](VirtualizationApi.md#virtualization_virtual_machines_delete) | **DELETE** /virtualization/virtual-machines/{id}/ | 
[**virtualization_virtual_machines_list**](VirtualizationApi.md#virtualization_virtual_machines_list) | **GET** /virtualization/virtual-machines/ | 
[**virtualization_virtual_machines_partial_update**](VirtualizationApi.md#virtualization_virtual_machines_partial_update) | **PATCH** /virtualization/virtual-machines/{id}/ | 
[**virtualization_virtual_machines_read**](VirtualizationApi.md#virtualization_virtual_machines_read) | **GET** /virtualization/virtual-machines/{id}/ | 
[**virtualization_virtual_machines_update**](VirtualizationApi.md#virtualization_virtual_machines_update) | **PUT** /virtualization/virtual-machines/{id}/ | 


# **virtualization_choices_list**
> virtualization_choices_list()





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
api_instance = aionetbox.VirtualizationApi(aionetbox.ApiClient(configuration))

try:
    api_instance.virtualization_choices_list()
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_choices_list: %s\n" % e)
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

# **virtualization_choices_read**
> virtualization_choices_read(id)





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
api_instance = aionetbox.VirtualizationApi(aionetbox.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.virtualization_choices_read(id)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_choices_read: %s\n" % e)
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

# **virtualization_cluster_groups_create**
> ClusterGroup virtualization_cluster_groups_create(data)





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
api_instance = aionetbox.VirtualizationApi(aionetbox.ApiClient(configuration))
data = aionetbox.ClusterGroup() # ClusterGroup | 

try:
    api_response = api_instance.virtualization_cluster_groups_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_cluster_groups_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ClusterGroup**](ClusterGroup.md)|  | 

### Return type

[**ClusterGroup**](ClusterGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_cluster_groups_delete**
> virtualization_cluster_groups_delete(id)





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
api_instance = aionetbox.VirtualizationApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cluster group.

try:
    api_instance.virtualization_cluster_groups_delete(id)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_cluster_groups_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cluster group. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_cluster_groups_list**
> InlineResponse20059 virtualization_cluster_groups_list(id=id, name=name, slug=slug, q=q, limit=limit, offset=offset)



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
api_instance = aionetbox.VirtualizationApi(aionetbox.ApiClient(configuration))
id = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
slug = 'slug_example' # str |  (optional)
q = 'q_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.virtualization_cluster_groups_list(id=id, name=name, slug=slug, q=q, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_cluster_groups_list: %s\n" % e)
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

[**InlineResponse20059**](InlineResponse20059.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_cluster_groups_partial_update**
> ClusterGroup virtualization_cluster_groups_partial_update(id, data)





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
api_instance = aionetbox.VirtualizationApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cluster group.
data = aionetbox.ClusterGroup() # ClusterGroup | 

try:
    api_response = api_instance.virtualization_cluster_groups_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_cluster_groups_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cluster group. | 
 **data** | [**ClusterGroup**](ClusterGroup.md)|  | 

### Return type

[**ClusterGroup**](ClusterGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_cluster_groups_read**
> ClusterGroup virtualization_cluster_groups_read(id)



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
api_instance = aionetbox.VirtualizationApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cluster group.

try:
    api_response = api_instance.virtualization_cluster_groups_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_cluster_groups_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cluster group. | 

### Return type

[**ClusterGroup**](ClusterGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_cluster_groups_update**
> ClusterGroup virtualization_cluster_groups_update(id, data)





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
api_instance = aionetbox.VirtualizationApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cluster group.
data = aionetbox.ClusterGroup() # ClusterGroup | 

try:
    api_response = api_instance.virtualization_cluster_groups_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_cluster_groups_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cluster group. | 
 **data** | [**ClusterGroup**](ClusterGroup.md)|  | 

### Return type

[**ClusterGroup**](ClusterGroup.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_cluster_types_create**
> ClusterType virtualization_cluster_types_create(data)





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
api_instance = aionetbox.VirtualizationApi(aionetbox.ApiClient(configuration))
data = aionetbox.ClusterType() # ClusterType | 

try:
    api_response = api_instance.virtualization_cluster_types_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_cluster_types_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ClusterType**](ClusterType.md)|  | 

### Return type

[**ClusterType**](ClusterType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_cluster_types_delete**
> virtualization_cluster_types_delete(id)





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
api_instance = aionetbox.VirtualizationApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cluster type.

try:
    api_instance.virtualization_cluster_types_delete(id)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_cluster_types_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cluster type. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_cluster_types_list**
> InlineResponse20060 virtualization_cluster_types_list(id=id, name=name, slug=slug, q=q, limit=limit, offset=offset)



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
api_instance = aionetbox.VirtualizationApi(aionetbox.ApiClient(configuration))
id = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
slug = 'slug_example' # str |  (optional)
q = 'q_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.virtualization_cluster_types_list(id=id, name=name, slug=slug, q=q, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_cluster_types_list: %s\n" % e)
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

[**InlineResponse20060**](InlineResponse20060.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_cluster_types_partial_update**
> ClusterType virtualization_cluster_types_partial_update(id, data)





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
api_instance = aionetbox.VirtualizationApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cluster type.
data = aionetbox.ClusterType() # ClusterType | 

try:
    api_response = api_instance.virtualization_cluster_types_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_cluster_types_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cluster type. | 
 **data** | [**ClusterType**](ClusterType.md)|  | 

### Return type

[**ClusterType**](ClusterType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_cluster_types_read**
> ClusterType virtualization_cluster_types_read(id)



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
api_instance = aionetbox.VirtualizationApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cluster type.

try:
    api_response = api_instance.virtualization_cluster_types_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_cluster_types_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cluster type. | 

### Return type

[**ClusterType**](ClusterType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_cluster_types_update**
> ClusterType virtualization_cluster_types_update(id, data)





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
api_instance = aionetbox.VirtualizationApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cluster type.
data = aionetbox.ClusterType() # ClusterType | 

try:
    api_response = api_instance.virtualization_cluster_types_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_cluster_types_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cluster type. | 
 **data** | [**ClusterType**](ClusterType.md)|  | 

### Return type

[**ClusterType**](ClusterType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_clusters_create**
> Cluster virtualization_clusters_create(data)





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
api_instance = aionetbox.VirtualizationApi(aionetbox.ApiClient(configuration))
data = aionetbox.WritableCluster() # WritableCluster | 

try:
    api_response = api_instance.virtualization_clusters_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_clusters_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WritableCluster**](WritableCluster.md)|  | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_clusters_delete**
> virtualization_clusters_delete(id)





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
api_instance = aionetbox.VirtualizationApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cluster.

try:
    api_instance.virtualization_clusters_delete(id)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_clusters_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cluster. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_clusters_list**
> InlineResponse20061 virtualization_clusters_list(name=name, id__in=id__in, q=q, group_id=group_id, group=group, type_id=type_id, type=type, site_id=site_id, site=site, tag=tag, limit=limit, offset=offset)



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
api_instance = aionetbox.VirtualizationApi(aionetbox.ApiClient(configuration))
name = 'name_example' # str |  (optional)
id__in = 'id__in_example' # str | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
group_id = 'group_id_example' # str |  (optional)
group = 'group_example' # str |  (optional)
type_id = 'type_id_example' # str |  (optional)
type = 'type_example' # str |  (optional)
site_id = 'site_id_example' # str |  (optional)
site = 'site_example' # str |  (optional)
tag = 'tag_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.virtualization_clusters_list(name=name, id__in=id__in, q=q, group_id=group_id, group=group, type_id=type_id, type=type, site_id=site_id, site=site, tag=tag, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_clusters_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **id__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **q** | **str**|  | [optional] 
 **group_id** | **str**|  | [optional] 
 **group** | **str**|  | [optional] 
 **type_id** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **site_id** | **str**|  | [optional] 
 **site** | **str**|  | [optional] 
 **tag** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20061**](InlineResponse20061.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_clusters_partial_update**
> Cluster virtualization_clusters_partial_update(id, data)





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
api_instance = aionetbox.VirtualizationApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cluster.
data = aionetbox.WritableCluster() # WritableCluster | 

try:
    api_response = api_instance.virtualization_clusters_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_clusters_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cluster. | 
 **data** | [**WritableCluster**](WritableCluster.md)|  | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_clusters_read**
> Cluster virtualization_clusters_read(id)



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
api_instance = aionetbox.VirtualizationApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cluster.

try:
    api_response = api_instance.virtualization_clusters_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_clusters_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cluster. | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_clusters_update**
> Cluster virtualization_clusters_update(id, data)





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
api_instance = aionetbox.VirtualizationApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this cluster.
data = aionetbox.WritableCluster() # WritableCluster | 

try:
    api_response = api_instance.virtualization_clusters_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_clusters_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this cluster. | 
 **data** | [**WritableCluster**](WritableCluster.md)|  | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_interfaces_create**
> VirtualMachineInterface virtualization_interfaces_create(data)





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
api_instance = aionetbox.VirtualizationApi(aionetbox.ApiClient(configuration))
data = aionetbox.WritableVirtualMachineInterface() # WritableVirtualMachineInterface | 

try:
    api_response = api_instance.virtualization_interfaces_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_interfaces_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WritableVirtualMachineInterface**](WritableVirtualMachineInterface.md)|  | 

### Return type

[**VirtualMachineInterface**](VirtualMachineInterface.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_interfaces_delete**
> virtualization_interfaces_delete(id)





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
api_instance = aionetbox.VirtualizationApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this interface.

try:
    api_instance.virtualization_interfaces_delete(id)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_interfaces_delete: %s\n" % e)
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

# **virtualization_interfaces_list**
> InlineResponse20062 virtualization_interfaces_list(id=id, name=name, enabled=enabled, mtu=mtu, q=q, virtual_machine_id=virtual_machine_id, virtual_machine=virtual_machine, mac_address=mac_address, limit=limit, offset=offset)



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
api_instance = aionetbox.VirtualizationApi(aionetbox.ApiClient(configuration))
id = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
enabled = 'enabled_example' # str |  (optional)
mtu = 'mtu_example' # str |  (optional)
q = 'q_example' # str |  (optional)
virtual_machine_id = 'virtual_machine_id_example' # str |  (optional)
virtual_machine = 'virtual_machine_example' # str |  (optional)
mac_address = 'mac_address_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.virtualization_interfaces_list(id=id, name=name, enabled=enabled, mtu=mtu, q=q, virtual_machine_id=virtual_machine_id, virtual_machine=virtual_machine, mac_address=mac_address, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_interfaces_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **enabled** | **str**|  | [optional] 
 **mtu** | **str**|  | [optional] 
 **q** | **str**|  | [optional] 
 **virtual_machine_id** | **str**|  | [optional] 
 **virtual_machine** | **str**|  | [optional] 
 **mac_address** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20062**](InlineResponse20062.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_interfaces_partial_update**
> VirtualMachineInterface virtualization_interfaces_partial_update(id, data)





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
api_instance = aionetbox.VirtualizationApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this interface.
data = aionetbox.WritableVirtualMachineInterface() # WritableVirtualMachineInterface | 

try:
    api_response = api_instance.virtualization_interfaces_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_interfaces_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this interface. | 
 **data** | [**WritableVirtualMachineInterface**](WritableVirtualMachineInterface.md)|  | 

### Return type

[**VirtualMachineInterface**](VirtualMachineInterface.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_interfaces_read**
> VirtualMachineInterface virtualization_interfaces_read(id)



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
api_instance = aionetbox.VirtualizationApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this interface.

try:
    api_response = api_instance.virtualization_interfaces_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_interfaces_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this interface. | 

### Return type

[**VirtualMachineInterface**](VirtualMachineInterface.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_interfaces_update**
> VirtualMachineInterface virtualization_interfaces_update(id, data)





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
api_instance = aionetbox.VirtualizationApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this interface.
data = aionetbox.WritableVirtualMachineInterface() # WritableVirtualMachineInterface | 

try:
    api_response = api_instance.virtualization_interfaces_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_interfaces_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this interface. | 
 **data** | [**WritableVirtualMachineInterface**](WritableVirtualMachineInterface.md)|  | 

### Return type

[**VirtualMachineInterface**](VirtualMachineInterface.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_virtual_machines_create**
> VirtualMachineWithConfigContext virtualization_virtual_machines_create(data)





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
api_instance = aionetbox.VirtualizationApi(aionetbox.ApiClient(configuration))
data = aionetbox.WritableVirtualMachineWithConfigContext() # WritableVirtualMachineWithConfigContext | 

try:
    api_response = api_instance.virtualization_virtual_machines_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_virtual_machines_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WritableVirtualMachineWithConfigContext**](WritableVirtualMachineWithConfigContext.md)|  | 

### Return type

[**VirtualMachineWithConfigContext**](VirtualMachineWithConfigContext.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_virtual_machines_delete**
> virtualization_virtual_machines_delete(id)





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
api_instance = aionetbox.VirtualizationApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this virtual machine.

try:
    api_instance.virtualization_virtual_machines_delete(id)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_virtual_machines_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this virtual machine. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_virtual_machines_list**
> InlineResponse20063 virtualization_virtual_machines_list(id=id, name=name, cluster=cluster, vcpus=vcpus, memory=memory, disk=disk, tenant_group_id=tenant_group_id, tenant_group=tenant_group, tenant_id=tenant_id, tenant=tenant, id__in=id__in, q=q, status=status, cluster_group_id=cluster_group_id, cluster_group=cluster_group, cluster_type_id=cluster_type_id, cluster_type=cluster_type, cluster_id=cluster_id, region_id=region_id, region=region, site_id=site_id, site=site, role_id=role_id, role=role, platform_id=platform_id, platform=platform, mac_address=mac_address, tag=tag, limit=limit, offset=offset)



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
api_instance = aionetbox.VirtualizationApi(aionetbox.ApiClient(configuration))
id = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
cluster = 'cluster_example' # str |  (optional)
vcpus = 'vcpus_example' # str |  (optional)
memory = 'memory_example' # str |  (optional)
disk = 'disk_example' # str |  (optional)
tenant_group_id = 'tenant_group_id_example' # str |  (optional)
tenant_group = 'tenant_group_example' # str |  (optional)
tenant_id = 'tenant_id_example' # str |  (optional)
tenant = 'tenant_example' # str |  (optional)
id__in = 'id__in_example' # str | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
status = 'status_example' # str |  (optional)
cluster_group_id = 'cluster_group_id_example' # str |  (optional)
cluster_group = 'cluster_group_example' # str |  (optional)
cluster_type_id = 'cluster_type_id_example' # str |  (optional)
cluster_type = 'cluster_type_example' # str |  (optional)
cluster_id = 'cluster_id_example' # str |  (optional)
region_id = 'region_id_example' # str |  (optional)
region = 'region_example' # str |  (optional)
site_id = 'site_id_example' # str |  (optional)
site = 'site_example' # str |  (optional)
role_id = 'role_id_example' # str |  (optional)
role = 'role_example' # str |  (optional)
platform_id = 'platform_id_example' # str |  (optional)
platform = 'platform_example' # str |  (optional)
mac_address = 'mac_address_example' # str |  (optional)
tag = 'tag_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.virtualization_virtual_machines_list(id=id, name=name, cluster=cluster, vcpus=vcpus, memory=memory, disk=disk, tenant_group_id=tenant_group_id, tenant_group=tenant_group, tenant_id=tenant_id, tenant=tenant, id__in=id__in, q=q, status=status, cluster_group_id=cluster_group_id, cluster_group=cluster_group, cluster_type_id=cluster_type_id, cluster_type=cluster_type, cluster_id=cluster_id, region_id=region_id, region=region, site_id=site_id, site=site, role_id=role_id, role=role, platform_id=platform_id, platform=platform, mac_address=mac_address, tag=tag, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_virtual_machines_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **cluster** | **str**|  | [optional] 
 **vcpus** | **str**|  | [optional] 
 **memory** | **str**|  | [optional] 
 **disk** | **str**|  | [optional] 
 **tenant_group_id** | **str**|  | [optional] 
 **tenant_group** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **tenant** | **str**|  | [optional] 
 **id__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **q** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **cluster_group_id** | **str**|  | [optional] 
 **cluster_group** | **str**|  | [optional] 
 **cluster_type_id** | **str**|  | [optional] 
 **cluster_type** | **str**|  | [optional] 
 **cluster_id** | **str**|  | [optional] 
 **region_id** | **str**|  | [optional] 
 **region** | **str**|  | [optional] 
 **site_id** | **str**|  | [optional] 
 **site** | **str**|  | [optional] 
 **role_id** | **str**|  | [optional] 
 **role** | **str**|  | [optional] 
 **platform_id** | **str**|  | [optional] 
 **platform** | **str**|  | [optional] 
 **mac_address** | **str**|  | [optional] 
 **tag** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20063**](InlineResponse20063.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_virtual_machines_partial_update**
> VirtualMachineWithConfigContext virtualization_virtual_machines_partial_update(id, data)





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
api_instance = aionetbox.VirtualizationApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this virtual machine.
data = aionetbox.WritableVirtualMachineWithConfigContext() # WritableVirtualMachineWithConfigContext | 

try:
    api_response = api_instance.virtualization_virtual_machines_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_virtual_machines_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this virtual machine. | 
 **data** | [**WritableVirtualMachineWithConfigContext**](WritableVirtualMachineWithConfigContext.md)|  | 

### Return type

[**VirtualMachineWithConfigContext**](VirtualMachineWithConfigContext.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_virtual_machines_read**
> VirtualMachineWithConfigContext virtualization_virtual_machines_read(id)



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
api_instance = aionetbox.VirtualizationApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this virtual machine.

try:
    api_response = api_instance.virtualization_virtual_machines_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_virtual_machines_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this virtual machine. | 

### Return type

[**VirtualMachineWithConfigContext**](VirtualMachineWithConfigContext.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **virtualization_virtual_machines_update**
> VirtualMachineWithConfigContext virtualization_virtual_machines_update(id, data)





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
api_instance = aionetbox.VirtualizationApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this virtual machine.
data = aionetbox.WritableVirtualMachineWithConfigContext() # WritableVirtualMachineWithConfigContext | 

try:
    api_response = api_instance.virtualization_virtual_machines_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VirtualizationApi->virtualization_virtual_machines_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this virtual machine. | 
 **data** | [**WritableVirtualMachineWithConfigContext**](WritableVirtualMachineWithConfigContext.md)|  | 

### Return type

[**VirtualMachineWithConfigContext**](VirtualMachineWithConfigContext.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

