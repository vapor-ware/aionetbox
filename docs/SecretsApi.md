# aionetbox.SecretsApi

All URIs are relative to *http://ceppi.ngrok.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**secrets_choices_list**](SecretsApi.md#secrets_choices_list) | **GET** /secrets/_choices/ | 
[**secrets_choices_read**](SecretsApi.md#secrets_choices_read) | **GET** /secrets/_choices/{id}/ | 
[**secrets_generate_rsa_key_pair_list**](SecretsApi.md#secrets_generate_rsa_key_pair_list) | **GET** /secrets/generate-rsa-key-pair/ | This endpoint can be used to generate a new RSA key pair. The keys are returned in PEM format.
[**secrets_get_session_key_create**](SecretsApi.md#secrets_get_session_key_create) | **POST** /secrets/get-session-key/ | 
[**secrets_secret_roles_create**](SecretsApi.md#secrets_secret_roles_create) | **POST** /secrets/secret-roles/ | 
[**secrets_secret_roles_delete**](SecretsApi.md#secrets_secret_roles_delete) | **DELETE** /secrets/secret-roles/{id}/ | 
[**secrets_secret_roles_list**](SecretsApi.md#secrets_secret_roles_list) | **GET** /secrets/secret-roles/ | 
[**secrets_secret_roles_partial_update**](SecretsApi.md#secrets_secret_roles_partial_update) | **PATCH** /secrets/secret-roles/{id}/ | 
[**secrets_secret_roles_read**](SecretsApi.md#secrets_secret_roles_read) | **GET** /secrets/secret-roles/{id}/ | 
[**secrets_secret_roles_update**](SecretsApi.md#secrets_secret_roles_update) | **PUT** /secrets/secret-roles/{id}/ | 
[**secrets_secrets_create**](SecretsApi.md#secrets_secrets_create) | **POST** /secrets/secrets/ | 
[**secrets_secrets_delete**](SecretsApi.md#secrets_secrets_delete) | **DELETE** /secrets/secrets/{id}/ | 
[**secrets_secrets_list**](SecretsApi.md#secrets_secrets_list) | **GET** /secrets/secrets/ | 
[**secrets_secrets_partial_update**](SecretsApi.md#secrets_secrets_partial_update) | **PATCH** /secrets/secrets/{id}/ | 
[**secrets_secrets_read**](SecretsApi.md#secrets_secrets_read) | **GET** /secrets/secrets/{id}/ | 
[**secrets_secrets_update**](SecretsApi.md#secrets_secrets_update) | **PUT** /secrets/secrets/{id}/ | 


# **secrets_choices_list**
> secrets_choices_list()





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
api_instance = aionetbox.SecretsApi(aionetbox.ApiClient(configuration))

try:
    api_instance.secrets_choices_list()
except ApiException as e:
    print("Exception when calling SecretsApi->secrets_choices_list: %s\n" % e)
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

# **secrets_choices_read**
> secrets_choices_read(id)





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
api_instance = aionetbox.SecretsApi(aionetbox.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.secrets_choices_read(id)
except ApiException as e:
    print("Exception when calling SecretsApi->secrets_choices_read: %s\n" % e)
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

# **secrets_generate_rsa_key_pair_list**
> secrets_generate_rsa_key_pair_list()

This endpoint can be used to generate a new RSA key pair. The keys are returned in PEM format.

{         \"public_key\": \"<public key>\",         \"private_key\": \"<private key>\"     }

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
api_instance = aionetbox.SecretsApi(aionetbox.ApiClient(configuration))

try:
    # This endpoint can be used to generate a new RSA key pair. The keys are returned in PEM format.
    api_instance.secrets_generate_rsa_key_pair_list()
except ApiException as e:
    print("Exception when calling SecretsApi->secrets_generate_rsa_key_pair_list: %s\n" % e)
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

# **secrets_get_session_key_create**
> secrets_get_session_key_create()



Retrieve a temporary session key to use for encrypting and decrypting secrets via the API. The user's private RSA key is POSTed with the name `private_key`. An example:      curl -v -X POST -H \"Authorization: Token <token>\" -H \"Accept: application/json; indent=4\" \\     --data-urlencode \"private_key@<filename>\" https://netbox/api/secrets/get-session-key/  This request will yield a base64-encoded session key to be included in an `X-Session-Key` header in future requests:      {         \"session_key\": \"+8t4SI6XikgVmB5+/urhozx9O5qCQANyOk1MNe6taRf=\"     }  This endpoint accepts one optional parameter: `preserve_key`. If True and a session key exists, the existing session key will be returned instead of a new one.

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
api_instance = aionetbox.SecretsApi(aionetbox.ApiClient(configuration))

try:
    api_instance.secrets_get_session_key_create()
except ApiException as e:
    print("Exception when calling SecretsApi->secrets_get_session_key_create: %s\n" % e)
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

# **secrets_secret_roles_create**
> SecretRole secrets_secret_roles_create(data)





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
api_instance = aionetbox.SecretsApi(aionetbox.ApiClient(configuration))
data = aionetbox.SecretRole() # SecretRole | 

try:
    api_response = api_instance.secrets_secret_roles_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsApi->secrets_secret_roles_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**SecretRole**](SecretRole.md)|  | 

### Return type

[**SecretRole**](SecretRole.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_secret_roles_delete**
> secrets_secret_roles_delete(id)





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
api_instance = aionetbox.SecretsApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this secret role.

try:
    api_instance.secrets_secret_roles_delete(id)
except ApiException as e:
    print("Exception when calling SecretsApi->secrets_secret_roles_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this secret role. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_secret_roles_list**
> InlineResponse20053 secrets_secret_roles_list(id=id, name=name, slug=slug, q=q, limit=limit, offset=offset)



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
api_instance = aionetbox.SecretsApi(aionetbox.ApiClient(configuration))
id = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
slug = 'slug_example' # str |  (optional)
q = 'q_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.secrets_secret_roles_list(id=id, name=name, slug=slug, q=q, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsApi->secrets_secret_roles_list: %s\n" % e)
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

[**InlineResponse20053**](InlineResponse20053.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_secret_roles_partial_update**
> SecretRole secrets_secret_roles_partial_update(id, data)





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
api_instance = aionetbox.SecretsApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this secret role.
data = aionetbox.SecretRole() # SecretRole | 

try:
    api_response = api_instance.secrets_secret_roles_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsApi->secrets_secret_roles_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this secret role. | 
 **data** | [**SecretRole**](SecretRole.md)|  | 

### Return type

[**SecretRole**](SecretRole.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_secret_roles_read**
> SecretRole secrets_secret_roles_read(id)



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
api_instance = aionetbox.SecretsApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this secret role.

try:
    api_response = api_instance.secrets_secret_roles_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsApi->secrets_secret_roles_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this secret role. | 

### Return type

[**SecretRole**](SecretRole.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_secret_roles_update**
> SecretRole secrets_secret_roles_update(id, data)





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
api_instance = aionetbox.SecretsApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this secret role.
data = aionetbox.SecretRole() # SecretRole | 

try:
    api_response = api_instance.secrets_secret_roles_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsApi->secrets_secret_roles_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this secret role. | 
 **data** | [**SecretRole**](SecretRole.md)|  | 

### Return type

[**SecretRole**](SecretRole.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_secrets_create**
> Secret secrets_secrets_create(data)





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
api_instance = aionetbox.SecretsApi(aionetbox.ApiClient(configuration))
data = aionetbox.WritableSecret() # WritableSecret | 

try:
    api_response = api_instance.secrets_secrets_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsApi->secrets_secrets_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WritableSecret**](WritableSecret.md)|  | 

### Return type

[**Secret**](Secret.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_secrets_delete**
> secrets_secrets_delete(id)





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
api_instance = aionetbox.SecretsApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this secret.

try:
    api_instance.secrets_secrets_delete(id)
except ApiException as e:
    print("Exception when calling SecretsApi->secrets_secrets_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this secret. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_secrets_list**
> InlineResponse20054 secrets_secrets_list(name=name, id__in=id__in, q=q, role_id=role_id, role=role, device_id=device_id, device=device, tag=tag, limit=limit, offset=offset)





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
api_instance = aionetbox.SecretsApi(aionetbox.ApiClient(configuration))
name = 'name_example' # str |  (optional)
id__in = 'id__in_example' # str | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
role_id = 'role_id_example' # str |  (optional)
role = 'role_example' # str |  (optional)
device_id = 'device_id_example' # str |  (optional)
device = 'device_example' # str |  (optional)
tag = 'tag_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.secrets_secrets_list(name=name, id__in=id__in, q=q, role_id=role_id, role=role, device_id=device_id, device=device, tag=tag, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsApi->secrets_secrets_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **id__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **q** | **str**|  | [optional] 
 **role_id** | **str**|  | [optional] 
 **role** | **str**|  | [optional] 
 **device_id** | **str**|  | [optional] 
 **device** | **str**|  | [optional] 
 **tag** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse20054**](InlineResponse20054.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_secrets_partial_update**
> Secret secrets_secrets_partial_update(id, data)





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
api_instance = aionetbox.SecretsApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this secret.
data = aionetbox.WritableSecret() # WritableSecret | 

try:
    api_response = api_instance.secrets_secrets_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsApi->secrets_secrets_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this secret. | 
 **data** | [**WritableSecret**](WritableSecret.md)|  | 

### Return type

[**Secret**](Secret.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_secrets_read**
> Secret secrets_secrets_read(id)





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
api_instance = aionetbox.SecretsApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this secret.

try:
    api_response = api_instance.secrets_secrets_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsApi->secrets_secrets_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this secret. | 

### Return type

[**Secret**](Secret.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **secrets_secrets_update**
> Secret secrets_secrets_update(id, data)





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
api_instance = aionetbox.SecretsApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this secret.
data = aionetbox.WritableSecret() # WritableSecret | 

try:
    api_response = api_instance.secrets_secrets_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecretsApi->secrets_secrets_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this secret. | 
 **data** | [**WritableSecret**](WritableSecret.md)|  | 

### Return type

[**Secret**](Secret.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

