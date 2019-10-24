# aionetbox.ExtrasApi

All URIs are relative to *http://ceppi.ngrok.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extras_choices_list**](ExtrasApi.md#extras_choices_list) | **GET** /extras/_choices/ | 
[**extras_choices_read**](ExtrasApi.md#extras_choices_read) | **GET** /extras/_choices/{id}/ | 
[**extras_config_contexts_create**](ExtrasApi.md#extras_config_contexts_create) | **POST** /extras/config-contexts/ | 
[**extras_config_contexts_delete**](ExtrasApi.md#extras_config_contexts_delete) | **DELETE** /extras/config-contexts/{id}/ | 
[**extras_config_contexts_list**](ExtrasApi.md#extras_config_contexts_list) | **GET** /extras/config-contexts/ | 
[**extras_config_contexts_partial_update**](ExtrasApi.md#extras_config_contexts_partial_update) | **PATCH** /extras/config-contexts/{id}/ | 
[**extras_config_contexts_read**](ExtrasApi.md#extras_config_contexts_read) | **GET** /extras/config-contexts/{id}/ | 
[**extras_config_contexts_update**](ExtrasApi.md#extras_config_contexts_update) | **PUT** /extras/config-contexts/{id}/ | 
[**extras_custom_field_choices_list**](ExtrasApi.md#extras_custom_field_choices_list) | **GET** /extras/_custom_field_choices/ | 
[**extras_custom_field_choices_read**](ExtrasApi.md#extras_custom_field_choices_read) | **GET** /extras/_custom_field_choices/{id}/ | 
[**extras_export_templates_create**](ExtrasApi.md#extras_export_templates_create) | **POST** /extras/export-templates/ | 
[**extras_export_templates_delete**](ExtrasApi.md#extras_export_templates_delete) | **DELETE** /extras/export-templates/{id}/ | 
[**extras_export_templates_list**](ExtrasApi.md#extras_export_templates_list) | **GET** /extras/export-templates/ | 
[**extras_export_templates_partial_update**](ExtrasApi.md#extras_export_templates_partial_update) | **PATCH** /extras/export-templates/{id}/ | 
[**extras_export_templates_read**](ExtrasApi.md#extras_export_templates_read) | **GET** /extras/export-templates/{id}/ | 
[**extras_export_templates_update**](ExtrasApi.md#extras_export_templates_update) | **PUT** /extras/export-templates/{id}/ | 
[**extras_graphs_create**](ExtrasApi.md#extras_graphs_create) | **POST** /extras/graphs/ | 
[**extras_graphs_delete**](ExtrasApi.md#extras_graphs_delete) | **DELETE** /extras/graphs/{id}/ | 
[**extras_graphs_list**](ExtrasApi.md#extras_graphs_list) | **GET** /extras/graphs/ | 
[**extras_graphs_partial_update**](ExtrasApi.md#extras_graphs_partial_update) | **PATCH** /extras/graphs/{id}/ | 
[**extras_graphs_read**](ExtrasApi.md#extras_graphs_read) | **GET** /extras/graphs/{id}/ | 
[**extras_graphs_update**](ExtrasApi.md#extras_graphs_update) | **PUT** /extras/graphs/{id}/ | 
[**extras_image_attachments_create**](ExtrasApi.md#extras_image_attachments_create) | **POST** /extras/image-attachments/ | 
[**extras_image_attachments_delete**](ExtrasApi.md#extras_image_attachments_delete) | **DELETE** /extras/image-attachments/{id}/ | 
[**extras_image_attachments_list**](ExtrasApi.md#extras_image_attachments_list) | **GET** /extras/image-attachments/ | 
[**extras_image_attachments_partial_update**](ExtrasApi.md#extras_image_attachments_partial_update) | **PATCH** /extras/image-attachments/{id}/ | 
[**extras_image_attachments_read**](ExtrasApi.md#extras_image_attachments_read) | **GET** /extras/image-attachments/{id}/ | 
[**extras_image_attachments_update**](ExtrasApi.md#extras_image_attachments_update) | **PUT** /extras/image-attachments/{id}/ | 
[**extras_object_changes_list**](ExtrasApi.md#extras_object_changes_list) | **GET** /extras/object-changes/ | 
[**extras_object_changes_read**](ExtrasApi.md#extras_object_changes_read) | **GET** /extras/object-changes/{id}/ | 
[**extras_reports_list**](ExtrasApi.md#extras_reports_list) | **GET** /extras/reports/ | 
[**extras_reports_read**](ExtrasApi.md#extras_reports_read) | **GET** /extras/reports/{id}/ | 
[**extras_reports_run**](ExtrasApi.md#extras_reports_run) | **POST** /extras/reports/{id}/run/ | 
[**extras_tags_create**](ExtrasApi.md#extras_tags_create) | **POST** /extras/tags/ | 
[**extras_tags_delete**](ExtrasApi.md#extras_tags_delete) | **DELETE** /extras/tags/{id}/ | 
[**extras_tags_list**](ExtrasApi.md#extras_tags_list) | **GET** /extras/tags/ | 
[**extras_tags_partial_update**](ExtrasApi.md#extras_tags_partial_update) | **PATCH** /extras/tags/{id}/ | 
[**extras_tags_read**](ExtrasApi.md#extras_tags_read) | **GET** /extras/tags/{id}/ | 
[**extras_tags_update**](ExtrasApi.md#extras_tags_update) | **PUT** /extras/tags/{id}/ | 
[**extras_topology_maps_create**](ExtrasApi.md#extras_topology_maps_create) | **POST** /extras/topology-maps/ | 
[**extras_topology_maps_delete**](ExtrasApi.md#extras_topology_maps_delete) | **DELETE** /extras/topology-maps/{id}/ | 
[**extras_topology_maps_list**](ExtrasApi.md#extras_topology_maps_list) | **GET** /extras/topology-maps/ | 
[**extras_topology_maps_partial_update**](ExtrasApi.md#extras_topology_maps_partial_update) | **PATCH** /extras/topology-maps/{id}/ | 
[**extras_topology_maps_read**](ExtrasApi.md#extras_topology_maps_read) | **GET** /extras/topology-maps/{id}/ | 
[**extras_topology_maps_render**](ExtrasApi.md#extras_topology_maps_render) | **GET** /extras/topology-maps/{id}/render/ | 
[**extras_topology_maps_update**](ExtrasApi.md#extras_topology_maps_update) | **PUT** /extras/topology-maps/{id}/ | 


# **extras_choices_list**
> extras_choices_list()





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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))

try:
    api_instance.extras_choices_list()
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_choices_list: %s\n" % e)
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

# **extras_choices_read**
> extras_choices_read(id)





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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.extras_choices_read(id)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_choices_read: %s\n" % e)
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

# **extras_config_contexts_create**
> ConfigContext extras_config_contexts_create(data)





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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
data = aionetbox.WritableConfigContext() # WritableConfigContext | 

try:
    api_response = api_instance.extras_config_contexts_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_config_contexts_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WritableConfigContext**](WritableConfigContext.md)|  | 

### Return type

[**ConfigContext**](ConfigContext.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_config_contexts_delete**
> extras_config_contexts_delete(id)





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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this config context.

try:
    api_instance.extras_config_contexts_delete(id)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_config_contexts_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this config context. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_config_contexts_list**
> InlineResponse20037 extras_config_contexts_list(name=name, is_active=is_active, q=q, region_id=region_id, region=region, site_id=site_id, site=site, role_id=role_id, role=role, platform_id=platform_id, platform=platform, tenant_group_id=tenant_group_id, tenant_group=tenant_group, tenant_id=tenant_id, tenant=tenant, limit=limit, offset=offset)



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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
name = 'name_example' # str |  (optional)
is_active = 'is_active_example' # str |  (optional)
q = 'q_example' # str |  (optional)
region_id = 'region_id_example' # str |  (optional)
region = 'region_example' # str |  (optional)
site_id = 'site_id_example' # str |  (optional)
site = 'site_example' # str |  (optional)
role_id = 'role_id_example' # str |  (optional)
role = 'role_example' # str |  (optional)
platform_id = 'platform_id_example' # str |  (optional)
platform = 'platform_example' # str |  (optional)
tenant_group_id = 'tenant_group_id_example' # str |  (optional)
tenant_group = 'tenant_group_example' # str |  (optional)
tenant_id = 'tenant_id_example' # str |  (optional)
tenant = 'tenant_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.extras_config_contexts_list(name=name, is_active=is_active, q=q, region_id=region_id, region=region, site_id=site_id, site=site, role_id=role_id, role=role, platform_id=platform_id, platform=platform, tenant_group_id=tenant_group_id, tenant_group=tenant_group, tenant_id=tenant_id, tenant=tenant, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_config_contexts_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **is_active** | **str**|  | [optional] 
 **q** | **str**|  | [optional] 
 **region_id** | **str**|  | [optional] 
 **region** | **str**|  | [optional] 
 **site_id** | **str**|  | [optional] 
 **site** | **str**|  | [optional] 
 **role_id** | **str**|  | [optional] 
 **role** | **str**|  | [optional] 
 **platform_id** | **str**|  | [optional] 
 **platform** | **str**|  | [optional] 
 **tenant_group_id** | **str**|  | [optional] 
 **tenant_group** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **tenant** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20037**](InlineResponse20037.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_config_contexts_partial_update**
> ConfigContext extras_config_contexts_partial_update(id, data)





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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this config context.
data = aionetbox.WritableConfigContext() # WritableConfigContext | 

try:
    api_response = api_instance.extras_config_contexts_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_config_contexts_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this config context. | 
 **data** | [**WritableConfigContext**](WritableConfigContext.md)|  | 

### Return type

[**ConfigContext**](ConfigContext.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_config_contexts_read**
> ConfigContext extras_config_contexts_read(id)



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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this config context.

try:
    api_response = api_instance.extras_config_contexts_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_config_contexts_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this config context. | 

### Return type

[**ConfigContext**](ConfigContext.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_config_contexts_update**
> ConfigContext extras_config_contexts_update(id, data)





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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this config context.
data = aionetbox.WritableConfigContext() # WritableConfigContext | 

try:
    api_response = api_instance.extras_config_contexts_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_config_contexts_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this config context. | 
 **data** | [**WritableConfigContext**](WritableConfigContext.md)|  | 

### Return type

[**ConfigContext**](ConfigContext.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_custom_field_choices_list**
> extras_custom_field_choices_list()





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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))

try:
    api_instance.extras_custom_field_choices_list()
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_custom_field_choices_list: %s\n" % e)
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

# **extras_custom_field_choices_read**
> extras_custom_field_choices_read(id)





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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.extras_custom_field_choices_read(id)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_custom_field_choices_read: %s\n" % e)
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

# **extras_export_templates_create**
> ExportTemplate extras_export_templates_create(data)





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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
data = aionetbox.WritableExportTemplate() # WritableExportTemplate | 

try:
    api_response = api_instance.extras_export_templates_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_export_templates_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WritableExportTemplate**](WritableExportTemplate.md)|  | 

### Return type

[**ExportTemplate**](ExportTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_export_templates_delete**
> extras_export_templates_delete(id)





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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this export template.

try:
    api_instance.extras_export_templates_delete(id)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_export_templates_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this export template. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_export_templates_list**
> InlineResponse20038 extras_export_templates_list(content_type=content_type, name=name, template_language=template_language, limit=limit, offset=offset)



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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
content_type = 'content_type_example' # str |  (optional)
name = 'name_example' # str |  (optional)
template_language = 'template_language_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.extras_export_templates_list(content_type=content_type, name=name, template_language=template_language, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_export_templates_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **template_language** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20038**](InlineResponse20038.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_export_templates_partial_update**
> ExportTemplate extras_export_templates_partial_update(id, data)





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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this export template.
data = aionetbox.WritableExportTemplate() # WritableExportTemplate | 

try:
    api_response = api_instance.extras_export_templates_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_export_templates_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this export template. | 
 **data** | [**WritableExportTemplate**](WritableExportTemplate.md)|  | 

### Return type

[**ExportTemplate**](ExportTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_export_templates_read**
> ExportTemplate extras_export_templates_read(id)



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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this export template.

try:
    api_response = api_instance.extras_export_templates_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_export_templates_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this export template. | 

### Return type

[**ExportTemplate**](ExportTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_export_templates_update**
> ExportTemplate extras_export_templates_update(id, data)





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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this export template.
data = aionetbox.WritableExportTemplate() # WritableExportTemplate | 

try:
    api_response = api_instance.extras_export_templates_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_export_templates_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this export template. | 
 **data** | [**WritableExportTemplate**](WritableExportTemplate.md)|  | 

### Return type

[**ExportTemplate**](ExportTemplate.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_graphs_create**
> Graph extras_graphs_create(data)





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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
data = aionetbox.WritableGraph() # WritableGraph | 

try:
    api_response = api_instance.extras_graphs_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_graphs_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WritableGraph**](WritableGraph.md)|  | 

### Return type

[**Graph**](Graph.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_graphs_delete**
> extras_graphs_delete(id)





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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this graph.

try:
    api_instance.extras_graphs_delete(id)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_graphs_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this graph. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_graphs_list**
> InlineResponse20039 extras_graphs_list(type=type, name=name, limit=limit, offset=offset)



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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
type = 'type_example' # str |  (optional)
name = 'name_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.extras_graphs_list(type=type, name=name, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_graphs_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20039**](InlineResponse20039.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_graphs_partial_update**
> Graph extras_graphs_partial_update(id, data)





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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this graph.
data = aionetbox.WritableGraph() # WritableGraph | 

try:
    api_response = api_instance.extras_graphs_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_graphs_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this graph. | 
 **data** | [**WritableGraph**](WritableGraph.md)|  | 

### Return type

[**Graph**](Graph.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_graphs_read**
> Graph extras_graphs_read(id)



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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this graph.

try:
    api_response = api_instance.extras_graphs_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_graphs_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this graph. | 

### Return type

[**Graph**](Graph.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_graphs_update**
> Graph extras_graphs_update(id, data)





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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this graph.
data = aionetbox.WritableGraph() # WritableGraph | 

try:
    api_response = api_instance.extras_graphs_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_graphs_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this graph. | 
 **data** | [**WritableGraph**](WritableGraph.md)|  | 

### Return type

[**Graph**](Graph.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_image_attachments_create**
> ImageAttachment extras_image_attachments_create(data)





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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
data = aionetbox.ImageAttachment() # ImageAttachment | 

try:
    api_response = api_instance.extras_image_attachments_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_image_attachments_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**ImageAttachment**](ImageAttachment.md)|  | 

### Return type

[**ImageAttachment**](ImageAttachment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_image_attachments_delete**
> extras_image_attachments_delete(id)





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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this image attachment.

try:
    api_instance.extras_image_attachments_delete(id)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_image_attachments_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this image attachment. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_image_attachments_list**
> InlineResponse20040 extras_image_attachments_list(limit=limit, offset=offset)



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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.extras_image_attachments_list(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_image_attachments_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20040**](InlineResponse20040.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_image_attachments_partial_update**
> ImageAttachment extras_image_attachments_partial_update(id, data)





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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this image attachment.
data = aionetbox.ImageAttachment() # ImageAttachment | 

try:
    api_response = api_instance.extras_image_attachments_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_image_attachments_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this image attachment. | 
 **data** | [**ImageAttachment**](ImageAttachment.md)|  | 

### Return type

[**ImageAttachment**](ImageAttachment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_image_attachments_read**
> ImageAttachment extras_image_attachments_read(id)



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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this image attachment.

try:
    api_response = api_instance.extras_image_attachments_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_image_attachments_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this image attachment. | 

### Return type

[**ImageAttachment**](ImageAttachment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_image_attachments_update**
> ImageAttachment extras_image_attachments_update(id, data)





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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this image attachment.
data = aionetbox.ImageAttachment() # ImageAttachment | 

try:
    api_response = api_instance.extras_image_attachments_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_image_attachments_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this image attachment. | 
 **data** | [**ImageAttachment**](ImageAttachment.md)|  | 

### Return type

[**ImageAttachment**](ImageAttachment.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_object_changes_list**
> InlineResponse20041 extras_object_changes_list(user=user, user_name=user_name, request_id=request_id, action=action, changed_object_type=changed_object_type, changed_object_id=changed_object_id, object_repr=object_repr, q=q, time=time, limit=limit, offset=offset)



Retrieve a list of recent changes.

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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
user = 'user_example' # str |  (optional)
user_name = 'user_name_example' # str |  (optional)
request_id = 'request_id_example' # str |  (optional)
action = 'action_example' # str |  (optional)
changed_object_type = 'changed_object_type_example' # str |  (optional)
changed_object_id = 8.14 # float |  (optional)
object_repr = 'object_repr_example' # str |  (optional)
q = 'q_example' # str |  (optional)
time = 'time_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.extras_object_changes_list(user=user, user_name=user_name, request_id=request_id, action=action, changed_object_type=changed_object_type, changed_object_id=changed_object_id, object_repr=object_repr, q=q, time=time, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_object_changes_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**|  | [optional] 
 **user_name** | **str**|  | [optional] 
 **request_id** | **str**|  | [optional] 
 **action** | **str**|  | [optional] 
 **changed_object_type** | **str**|  | [optional] 
 **changed_object_id** | **float**|  | [optional] 
 **object_repr** | **str**|  | [optional] 
 **q** | **str**|  | [optional] 
 **time** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20041**](InlineResponse20041.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_object_changes_read**
> ObjectChange extras_object_changes_read(id)



Retrieve a list of recent changes.

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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this object change.

try:
    api_response = api_instance.extras_object_changes_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_object_changes_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this object change. | 

### Return type

[**ObjectChange**](ObjectChange.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_reports_list**
> extras_reports_list()



Compile all reports and their related results (if any). Result data is deferred in the list view.

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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))

try:
    api_instance.extras_reports_list()
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_reports_list: %s\n" % e)
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

# **extras_reports_read**
> extras_reports_read(id)



Retrieve a single Report identified as \"<module>.<report>\".

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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.extras_reports_read(id)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_reports_read: %s\n" % e)
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

# **extras_reports_run**
> extras_reports_run(id)



Run a Report and create a new ReportResult, overwriting any previous result for the Report.

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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.extras_reports_run(id)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_reports_run: %s\n" % e)
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

# **extras_tags_create**
> Tag extras_tags_create(data)





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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
data = aionetbox.Tag() # Tag | 

try:
    api_response = api_instance.extras_tags_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_tags_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Tag**](Tag.md)|  | 

### Return type

[**Tag**](Tag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_tags_delete**
> extras_tags_delete(id)





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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tag.

try:
    api_instance.extras_tags_delete(id)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_tags_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tag. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_tags_list**
> InlineResponse20042 extras_tags_list(name=name, slug=slug, q=q, limit=limit, offset=offset)



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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
name = 'name_example' # str |  (optional)
slug = 'slug_example' # str |  (optional)
q = 'q_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.extras_tags_list(name=name, slug=slug, q=q, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_tags_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **slug** | **str**|  | [optional] 
 **q** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20042**](InlineResponse20042.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_tags_partial_update**
> Tag extras_tags_partial_update(id, data)





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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tag.
data = aionetbox.Tag() # Tag | 

try:
    api_response = api_instance.extras_tags_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_tags_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tag. | 
 **data** | [**Tag**](Tag.md)|  | 

### Return type

[**Tag**](Tag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_tags_read**
> Tag extras_tags_read(id)



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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tag.

try:
    api_response = api_instance.extras_tags_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_tags_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tag. | 

### Return type

[**Tag**](Tag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_tags_update**
> Tag extras_tags_update(id, data)





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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this tag.
data = aionetbox.Tag() # Tag | 

try:
    api_response = api_instance.extras_tags_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_tags_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this tag. | 
 **data** | [**Tag**](Tag.md)|  | 

### Return type

[**Tag**](Tag.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_topology_maps_create**
> TopologyMap extras_topology_maps_create(data)





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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
data = aionetbox.WritableTopologyMap() # WritableTopologyMap | 

try:
    api_response = api_instance.extras_topology_maps_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_topology_maps_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WritableTopologyMap**](WritableTopologyMap.md)|  | 

### Return type

[**TopologyMap**](TopologyMap.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_topology_maps_delete**
> extras_topology_maps_delete(id)





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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this topology map.

try:
    api_instance.extras_topology_maps_delete(id)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_topology_maps_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this topology map. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_topology_maps_list**
> InlineResponse20043 extras_topology_maps_list(name=name, slug=slug, site_id=site_id, site=site, limit=limit, offset=offset)



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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
name = 'name_example' # str |  (optional)
slug = 'slug_example' # str |  (optional)
site_id = 'site_id_example' # str |  (optional)
site = 'site_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.extras_topology_maps_list(name=name, slug=slug, site_id=site_id, site=site, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_topology_maps_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **slug** | **str**|  | [optional] 
 **site_id** | **str**|  | [optional] 
 **site** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20043**](InlineResponse20043.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_topology_maps_partial_update**
> TopologyMap extras_topology_maps_partial_update(id, data)





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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this topology map.
data = aionetbox.WritableTopologyMap() # WritableTopologyMap | 

try:
    api_response = api_instance.extras_topology_maps_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_topology_maps_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this topology map. | 
 **data** | [**WritableTopologyMap**](WritableTopologyMap.md)|  | 

### Return type

[**TopologyMap**](TopologyMap.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_topology_maps_read**
> TopologyMap extras_topology_maps_read(id)



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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this topology map.

try:
    api_response = api_instance.extras_topology_maps_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_topology_maps_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this topology map. | 

### Return type

[**TopologyMap**](TopologyMap.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_topology_maps_render**
> TopologyMap extras_topology_maps_render(id)





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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this topology map.

try:
    api_response = api_instance.extras_topology_maps_render(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_topology_maps_render: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this topology map. | 

### Return type

[**TopologyMap**](TopologyMap.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extras_topology_maps_update**
> TopologyMap extras_topology_maps_update(id, data)





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
api_instance = aionetbox.ExtrasApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this topology map.
data = aionetbox.WritableTopologyMap() # WritableTopologyMap | 

try:
    api_response = api_instance.extras_topology_maps_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtrasApi->extras_topology_maps_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this topology map. | 
 **data** | [**WritableTopologyMap**](WritableTopologyMap.md)|  | 

### Return type

[**TopologyMap**](TopologyMap.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

