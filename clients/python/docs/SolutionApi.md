# SolviceRoutingClient.SolutionApi

All URIs are relative to *https://api.solvice.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_solution**](SolutionApi.md#get_solution) | **GET** /jobs/{jobId}/solution | Solution

# **get_solution**
> RoutingSolution get_solution(job_id)

Solution

Returns the actual solution of the routing problem. Only present when the status is `SOLVED`.

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
api_instance = SolviceRoutingClient.SolutionApi(SolviceRoutingClient.ApiClient(configuration))
job_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The job ID.

try:
    # Solution
    api_response = api_instance.get_solution(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SolutionApi->get_solution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | [**str**](.md)| The job ID. | 

### Return type

[**RoutingSolution**](RoutingSolution.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

