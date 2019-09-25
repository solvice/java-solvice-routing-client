# SolviceRoutingClient.RoutingApi

All URIs are relative to *https://api.solvice.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**evaluate**](RoutingApi.md#evaluate) | **POST** /evaluate | Evaluate
[**solve**](RoutingApi.md#solve) | **POST** /solve | Solve

# **evaluate**
> Object evaluate(body=body)

Evaluate

Evaluates any problem defined underneath. Result is the job id and its status. Fetch the solution immediately in the response.

### Example
```python
from __future__ import print_function
import time
import SolviceRoutingClient
from SolviceRoutingClient.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = SolviceRoutingClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = SolviceRoutingClient.RoutingApi(SolviceRoutingClient.ApiClient(configuration))
body = SolviceRoutingClient.Object() # Object | Problem solve request (optional)

try:
    # Evaluate
    api_response = api_instance.evaluate(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->evaluate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Object**](Object.md)| Problem solve request | [optional] 

### Return type

[**Object**](Object.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **solve**
> Job solve(body=body)

Solve

Solves any problem defined underneath. Result is the job id and its status. Fetch the solution afterwards in the Solution endpoint.

### Example
```python
from __future__ import print_function
import time
import SolviceRoutingClient
from SolviceRoutingClient.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = SolviceRoutingClient.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = SolviceRoutingClient.RoutingApi(SolviceRoutingClient.ApiClient(configuration))
body = SolviceRoutingClient.Object() # Object | Problem solve request (optional)

try:
    # Solve
    api_response = api_instance.solve(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoutingApi->solve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Object**](Object.md)| Problem solve request | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

