# SolviceRoutingClient.PVRPApi

All URIs are relative to *https://api.solvice.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**solve_pvrp**](PVRPApi.md#solve_pvrp) | **POST** /solve#PVRP | Solve a PVRP problem

# **solve_pvrp**
> Job solve_pvrp(body=body)

Solve a PVRP problem

Periodic vehicle routing problems

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
api_instance = SolviceRoutingClient.PVRPApi(SolviceRoutingClient.ApiClient(configuration))
body = SolviceRoutingClient.PVRP() # PVRP | PVRP problem solve request (optional)

try:
    # Solve a PVRP problem
    api_response = api_instance.solve_pvrp(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PVRPApi->solve_pvrp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PVRP**](PVRP.md)| PVRP problem solve request | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

