# aionetbox.CircuitsApi

All URIs are relative to *http://ceppi.ngrok.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**circuits_choices_list**](CircuitsApi.md#circuits_choices_list) | **GET** /circuits/_choices/ | 
[**circuits_choices_read**](CircuitsApi.md#circuits_choices_read) | **GET** /circuits/_choices/{id}/ | 
[**circuits_circuit_terminations_create**](CircuitsApi.md#circuits_circuit_terminations_create) | **POST** /circuits/circuit-terminations/ | 
[**circuits_circuit_terminations_delete**](CircuitsApi.md#circuits_circuit_terminations_delete) | **DELETE** /circuits/circuit-terminations/{id}/ | 
[**circuits_circuit_terminations_list**](CircuitsApi.md#circuits_circuit_terminations_list) | **GET** /circuits/circuit-terminations/ | 
[**circuits_circuit_terminations_partial_update**](CircuitsApi.md#circuits_circuit_terminations_partial_update) | **PATCH** /circuits/circuit-terminations/{id}/ | 
[**circuits_circuit_terminations_read**](CircuitsApi.md#circuits_circuit_terminations_read) | **GET** /circuits/circuit-terminations/{id}/ | 
[**circuits_circuit_terminations_update**](CircuitsApi.md#circuits_circuit_terminations_update) | **PUT** /circuits/circuit-terminations/{id}/ | 
[**circuits_circuit_types_create**](CircuitsApi.md#circuits_circuit_types_create) | **POST** /circuits/circuit-types/ | 
[**circuits_circuit_types_delete**](CircuitsApi.md#circuits_circuit_types_delete) | **DELETE** /circuits/circuit-types/{id}/ | 
[**circuits_circuit_types_list**](CircuitsApi.md#circuits_circuit_types_list) | **GET** /circuits/circuit-types/ | 
[**circuits_circuit_types_partial_update**](CircuitsApi.md#circuits_circuit_types_partial_update) | **PATCH** /circuits/circuit-types/{id}/ | 
[**circuits_circuit_types_read**](CircuitsApi.md#circuits_circuit_types_read) | **GET** /circuits/circuit-types/{id}/ | 
[**circuits_circuit_types_update**](CircuitsApi.md#circuits_circuit_types_update) | **PUT** /circuits/circuit-types/{id}/ | 
[**circuits_circuits_create**](CircuitsApi.md#circuits_circuits_create) | **POST** /circuits/circuits/ | 
[**circuits_circuits_delete**](CircuitsApi.md#circuits_circuits_delete) | **DELETE** /circuits/circuits/{id}/ | 
[**circuits_circuits_list**](CircuitsApi.md#circuits_circuits_list) | **GET** /circuits/circuits/ | 
[**circuits_circuits_partial_update**](CircuitsApi.md#circuits_circuits_partial_update) | **PATCH** /circuits/circuits/{id}/ | 
[**circuits_circuits_read**](CircuitsApi.md#circuits_circuits_read) | **GET** /circuits/circuits/{id}/ | 
[**circuits_circuits_update**](CircuitsApi.md#circuits_circuits_update) | **PUT** /circuits/circuits/{id}/ | 
[**circuits_providers_create**](CircuitsApi.md#circuits_providers_create) | **POST** /circuits/providers/ | 
[**circuits_providers_delete**](CircuitsApi.md#circuits_providers_delete) | **DELETE** /circuits/providers/{id}/ | 
[**circuits_providers_graphs**](CircuitsApi.md#circuits_providers_graphs) | **GET** /circuits/providers/{id}/graphs/ | 
[**circuits_providers_list**](CircuitsApi.md#circuits_providers_list) | **GET** /circuits/providers/ | 
[**circuits_providers_partial_update**](CircuitsApi.md#circuits_providers_partial_update) | **PATCH** /circuits/providers/{id}/ | 
[**circuits_providers_read**](CircuitsApi.md#circuits_providers_read) | **GET** /circuits/providers/{id}/ | 
[**circuits_providers_update**](CircuitsApi.md#circuits_providers_update) | **PUT** /circuits/providers/{id}/ | 


# **circuits_choices_list**
> circuits_choices_list()





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
api_instance = aionetbox.CircuitsApi(aionetbox.ApiClient(configuration))

try:
    api_instance.circuits_choices_list()
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_choices_list: %s\n" % e)
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

# **circuits_choices_read**
> circuits_choices_read(id)





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
api_instance = aionetbox.CircuitsApi(aionetbox.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.circuits_choices_read(id)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_choices_read: %s\n" % e)
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

# **circuits_circuit_terminations_create**
> CircuitTermination circuits_circuit_terminations_create(data)





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
api_instance = aionetbox.CircuitsApi(aionetbox.ApiClient(configuration))
data = aionetbox.WritableCircuitTermination() # WritableCircuitTermination | 

try:
    api_response = api_instance.circuits_circuit_terminations_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_circuit_terminations_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WritableCircuitTermination**](WritableCircuitTermination.md)|  | 

### Return type

[**CircuitTermination**](CircuitTermination.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_circuit_terminations_delete**
> circuits_circuit_terminations_delete(id)





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
api_instance = aionetbox.CircuitsApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this circuit termination.

try:
    api_instance.circuits_circuit_terminations_delete(id)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_circuit_terminations_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this circuit termination. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_circuit_terminations_list**
> InlineResponse200 circuits_circuit_terminations_list(term_side=term_side, port_speed=port_speed, upstream_speed=upstream_speed, xconnect_id=xconnect_id, q=q, circuit_id=circuit_id, site_id=site_id, site=site, limit=limit, offset=offset)



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
api_instance = aionetbox.CircuitsApi(aionetbox.ApiClient(configuration))
term_side = 'term_side_example' # str |  (optional)
port_speed = 'port_speed_example' # str |  (optional)
upstream_speed = 'upstream_speed_example' # str |  (optional)
xconnect_id = 'xconnect_id_example' # str |  (optional)
q = 'q_example' # str |  (optional)
circuit_id = 'circuit_id_example' # str |  (optional)
site_id = 'site_id_example' # str |  (optional)
site = 'site_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.circuits_circuit_terminations_list(term_side=term_side, port_speed=port_speed, upstream_speed=upstream_speed, xconnect_id=xconnect_id, q=q, circuit_id=circuit_id, site_id=site_id, site=site, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_circuit_terminations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_side** | **str**|  | [optional] 
 **port_speed** | **str**|  | [optional] 
 **upstream_speed** | **str**|  | [optional] 
 **xconnect_id** | **str**|  | [optional] 
 **q** | **str**|  | [optional] 
 **circuit_id** | **str**|  | [optional] 
 **site_id** | **str**|  | [optional] 
 **site** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_circuit_terminations_partial_update**
> CircuitTermination circuits_circuit_terminations_partial_update(id, data)





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
api_instance = aionetbox.CircuitsApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this circuit termination.
data = aionetbox.WritableCircuitTermination() # WritableCircuitTermination | 

try:
    api_response = api_instance.circuits_circuit_terminations_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_circuit_terminations_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this circuit termination. | 
 **data** | [**WritableCircuitTermination**](WritableCircuitTermination.md)|  | 

### Return type

[**CircuitTermination**](CircuitTermination.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_circuit_terminations_read**
> CircuitTermination circuits_circuit_terminations_read(id)



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
api_instance = aionetbox.CircuitsApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this circuit termination.

try:
    api_response = api_instance.circuits_circuit_terminations_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_circuit_terminations_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this circuit termination. | 

### Return type

[**CircuitTermination**](CircuitTermination.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_circuit_terminations_update**
> CircuitTermination circuits_circuit_terminations_update(id, data)





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
api_instance = aionetbox.CircuitsApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this circuit termination.
data = aionetbox.WritableCircuitTermination() # WritableCircuitTermination | 

try:
    api_response = api_instance.circuits_circuit_terminations_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_circuit_terminations_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this circuit termination. | 
 **data** | [**WritableCircuitTermination**](WritableCircuitTermination.md)|  | 

### Return type

[**CircuitTermination**](CircuitTermination.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_circuit_types_create**
> CircuitType circuits_circuit_types_create(data)





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
api_instance = aionetbox.CircuitsApi(aionetbox.ApiClient(configuration))
data = aionetbox.CircuitType() # CircuitType | 

try:
    api_response = api_instance.circuits_circuit_types_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_circuit_types_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**CircuitType**](CircuitType.md)|  | 

### Return type

[**CircuitType**](CircuitType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_circuit_types_delete**
> circuits_circuit_types_delete(id)





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
api_instance = aionetbox.CircuitsApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this circuit type.

try:
    api_instance.circuits_circuit_types_delete(id)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_circuit_types_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this circuit type. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_circuit_types_list**
> InlineResponse2001 circuits_circuit_types_list(id=id, name=name, slug=slug, q=q, limit=limit, offset=offset)



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
api_instance = aionetbox.CircuitsApi(aionetbox.ApiClient(configuration))
id = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
slug = 'slug_example' # str |  (optional)
q = 'q_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.circuits_circuit_types_list(id=id, name=name, slug=slug, q=q, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_circuit_types_list: %s\n" % e)
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

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_circuit_types_partial_update**
> CircuitType circuits_circuit_types_partial_update(id, data)





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
api_instance = aionetbox.CircuitsApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this circuit type.
data = aionetbox.CircuitType() # CircuitType | 

try:
    api_response = api_instance.circuits_circuit_types_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_circuit_types_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this circuit type. | 
 **data** | [**CircuitType**](CircuitType.md)|  | 

### Return type

[**CircuitType**](CircuitType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_circuit_types_read**
> CircuitType circuits_circuit_types_read(id)



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
api_instance = aionetbox.CircuitsApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this circuit type.

try:
    api_response = api_instance.circuits_circuit_types_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_circuit_types_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this circuit type. | 

### Return type

[**CircuitType**](CircuitType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_circuit_types_update**
> CircuitType circuits_circuit_types_update(id, data)





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
api_instance = aionetbox.CircuitsApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this circuit type.
data = aionetbox.CircuitType() # CircuitType | 

try:
    api_response = api_instance.circuits_circuit_types_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_circuit_types_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this circuit type. | 
 **data** | [**CircuitType**](CircuitType.md)|  | 

### Return type

[**CircuitType**](CircuitType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_circuits_create**
> Circuit circuits_circuits_create(data)





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
api_instance = aionetbox.CircuitsApi(aionetbox.ApiClient(configuration))
data = aionetbox.WritableCircuit() # WritableCircuit | 

try:
    api_response = api_instance.circuits_circuits_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_circuits_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WritableCircuit**](WritableCircuit.md)|  | 

### Return type

[**Circuit**](Circuit.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_circuits_delete**
> circuits_circuits_delete(id)





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
api_instance = aionetbox.CircuitsApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this circuit.

try:
    api_instance.circuits_circuits_delete(id)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_circuits_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this circuit. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_circuits_list**
> InlineResponse2002 circuits_circuits_list(cid=cid, install_date=install_date, commit_rate=commit_rate, tenant_group_id=tenant_group_id, tenant_group=tenant_group, tenant_id=tenant_id, tenant=tenant, id__in=id__in, q=q, provider_id=provider_id, provider=provider, type_id=type_id, type=type, status=status, site_id=site_id, site=site, region_id=region_id, region=region, tag=tag, limit=limit, offset=offset)



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
api_instance = aionetbox.CircuitsApi(aionetbox.ApiClient(configuration))
cid = 'cid_example' # str |  (optional)
install_date = 'install_date_example' # str |  (optional)
commit_rate = 'commit_rate_example' # str |  (optional)
tenant_group_id = 'tenant_group_id_example' # str |  (optional)
tenant_group = 'tenant_group_example' # str |  (optional)
tenant_id = 'tenant_id_example' # str |  (optional)
tenant = 'tenant_example' # str |  (optional)
id__in = 'id__in_example' # str | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
provider_id = 'provider_id_example' # str |  (optional)
provider = 'provider_example' # str |  (optional)
type_id = 'type_id_example' # str |  (optional)
type = 'type_example' # str |  (optional)
status = 'status_example' # str |  (optional)
site_id = 'site_id_example' # str |  (optional)
site = 'site_example' # str |  (optional)
region_id = 'region_id_example' # str |  (optional)
region = 'region_example' # str |  (optional)
tag = 'tag_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.circuits_circuits_list(cid=cid, install_date=install_date, commit_rate=commit_rate, tenant_group_id=tenant_group_id, tenant_group=tenant_group, tenant_id=tenant_id, tenant=tenant, id__in=id__in, q=q, provider_id=provider_id, provider=provider, type_id=type_id, type=type, status=status, site_id=site_id, site=site, region_id=region_id, region=region, tag=tag, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_circuits_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cid** | **str**|  | [optional] 
 **install_date** | **str**|  | [optional] 
 **commit_rate** | **str**|  | [optional] 
 **tenant_group_id** | **str**|  | [optional] 
 **tenant_group** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **tenant** | **str**|  | [optional] 
 **id__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **q** | **str**|  | [optional] 
 **provider_id** | **str**|  | [optional] 
 **provider** | **str**|  | [optional] 
 **type_id** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **site_id** | **str**|  | [optional] 
 **site** | **str**|  | [optional] 
 **region_id** | **str**|  | [optional] 
 **region** | **str**|  | [optional] 
 **tag** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_circuits_partial_update**
> Circuit circuits_circuits_partial_update(id, data)





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
api_instance = aionetbox.CircuitsApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this circuit.
data = aionetbox.WritableCircuit() # WritableCircuit | 

try:
    api_response = api_instance.circuits_circuits_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_circuits_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this circuit. | 
 **data** | [**WritableCircuit**](WritableCircuit.md)|  | 

### Return type

[**Circuit**](Circuit.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_circuits_read**
> Circuit circuits_circuits_read(id)



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
api_instance = aionetbox.CircuitsApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this circuit.

try:
    api_response = api_instance.circuits_circuits_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_circuits_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this circuit. | 

### Return type

[**Circuit**](Circuit.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_circuits_update**
> Circuit circuits_circuits_update(id, data)





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
api_instance = aionetbox.CircuitsApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this circuit.
data = aionetbox.WritableCircuit() # WritableCircuit | 

try:
    api_response = api_instance.circuits_circuits_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_circuits_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this circuit. | 
 **data** | [**WritableCircuit**](WritableCircuit.md)|  | 

### Return type

[**Circuit**](Circuit.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_providers_create**
> Provider circuits_providers_create(data)





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
api_instance = aionetbox.CircuitsApi(aionetbox.ApiClient(configuration))
data = aionetbox.Provider() # Provider | 

try:
    api_response = api_instance.circuits_providers_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_providers_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Provider**](Provider.md)|  | 

### Return type

[**Provider**](Provider.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_providers_delete**
> circuits_providers_delete(id)





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
api_instance = aionetbox.CircuitsApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this provider.

try:
    api_instance.circuits_providers_delete(id)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_providers_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this provider. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_providers_graphs**
> Provider circuits_providers_graphs(id)



A convenience method for rendering graphs for a particular provider.

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
api_instance = aionetbox.CircuitsApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this provider.

try:
    api_response = api_instance.circuits_providers_graphs(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_providers_graphs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this provider. | 

### Return type

[**Provider**](Provider.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_providers_list**
> InlineResponse2003 circuits_providers_list(name=name, slug=slug, asn=asn, account=account, id__in=id__in, q=q, site_id=site_id, site=site, tag=tag, limit=limit, offset=offset)



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
api_instance = aionetbox.CircuitsApi(aionetbox.ApiClient(configuration))
name = 'name_example' # str |  (optional)
slug = 'slug_example' # str |  (optional)
asn = 'asn_example' # str |  (optional)
account = 'account_example' # str |  (optional)
id__in = 'id__in_example' # str | Multiple values may be separated by commas. (optional)
q = 'q_example' # str |  (optional)
site_id = 'site_id_example' # str |  (optional)
site = 'site_example' # str |  (optional)
tag = 'tag_example' # str |  (optional)
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.circuits_providers_list(name=name, slug=slug, asn=asn, account=account, id__in=id__in, q=q, site_id=site_id, site=site, tag=tag, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_providers_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **slug** | **str**|  | [optional] 
 **asn** | **str**|  | [optional] 
 **account** | **str**|  | [optional] 
 **id__in** | **str**| Multiple values may be separated by commas. | [optional] 
 **q** | **str**|  | [optional] 
 **site_id** | **str**|  | [optional] 
 **site** | **str**|  | [optional] 
 **tag** | **str**|  | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_providers_partial_update**
> Provider circuits_providers_partial_update(id, data)





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
api_instance = aionetbox.CircuitsApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this provider.
data = aionetbox.Provider() # Provider | 

try:
    api_response = api_instance.circuits_providers_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_providers_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this provider. | 
 **data** | [**Provider**](Provider.md)|  | 

### Return type

[**Provider**](Provider.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_providers_read**
> Provider circuits_providers_read(id)



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
api_instance = aionetbox.CircuitsApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this provider.

try:
    api_response = api_instance.circuits_providers_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_providers_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this provider. | 

### Return type

[**Provider**](Provider.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **circuits_providers_update**
> Provider circuits_providers_update(id, data)





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
api_instance = aionetbox.CircuitsApi(aionetbox.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this provider.
data = aionetbox.Provider() # Provider | 

try:
    api_response = api_instance.circuits_providers_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitsApi->circuits_providers_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this provider. | 
 **data** | [**Provider**](Provider.md)|  | 

### Return type

[**Provider**](Provider.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

