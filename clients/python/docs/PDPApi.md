# SolviceRoutingClient.PDPApi

All URIs are relative to *https://api.solvice.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_job_status**](PDPApi.md#get_job_status) | **GET** /jobs/{jobId}/status | Status
[**get_solution_pdp**](PDPApi.md#get_solution_pdp) | **GET** /jobs/{jobId}/solution#PDP | Solution PDP
[**solve_pdp**](PDPApi.md#solve_pdp) | **POST** /solve#PDP | Solve a PDP problem

# **get_job_status**
> Job get_job_status(job_id)

Status

Retrieve a specific job status

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
api_instance = SolviceRoutingClient.PDPApi(SolviceRoutingClient.ApiClient(configuration))
job_id = 'job_id_example' # str | The job ID.

try:
    # Status
    api_response = api_instance.get_job_status(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PDPApi->get_job_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| The job ID. | 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_solution_pdp**
> RoutingSolution get_solution_pdp(job_id)

Solution PDP

Returns the actual solution of the PDP. Only present when the status is `SOLVED`.

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
api_instance = SolviceRoutingClient.PDPApi(SolviceRoutingClient.ApiClient(configuration))
job_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The job ID.

try:
    # Solution PDP
    api_response = api_instance.get_solution_pdp(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PDPApi->get_solution_pdp: %s\n" % e)
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

# **solve_pdp**
> Job solve_pdp(body=body)

Solve a PDP problem

Pickup and delivery problems

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
api_instance = SolviceRoutingClient.PDPApi(SolviceRoutingClient.ApiClient(configuration))
body = SolviceRoutingClient.PDP() # PDP | PDP problem solve request (optional)

try:
    # Solve a PDP problem
    api_response = api_instance.solve_pdp(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PDPApi->solve_pdp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PDP**](PDP.md)| PDP problem solve request | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

