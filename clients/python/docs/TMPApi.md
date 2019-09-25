# SolviceRoutingClient.TMPApi

All URIs are relative to *https://api.solvice.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_job_status**](TMPApi.md#get_job_status) | **GET** /jobs/{jobId}/status | Status
[**solve_tmp**](TMPApi.md#solve_tmp) | **POST** /solve#TMP | solve a TMP problem

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
api_instance = SolviceRoutingClient.TMPApi(SolviceRoutingClient.ApiClient(configuration))
job_id = 'job_id_example' # str | The job ID.

try:
    # Status
    api_response = api_instance.get_job_status(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TMPApi->get_job_status: %s\n" % e)
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

# **solve_tmp**
> Job solve_tmp(body=body)

solve a TMP problem

Solves a TMP problem

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
api_instance = SolviceRoutingClient.TMPApi(SolviceRoutingClient.ApiClient(configuration))
body = SolviceRoutingClient.TMP() # TMP | TMP problem solve request (optional)

try:
    # solve a TMP problem
    api_response = api_instance.solve_tmp(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TMPApi->solve_tmp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TMP**](TMP.md)| TMP problem solve request | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

