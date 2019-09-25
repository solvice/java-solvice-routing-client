# swagger_client.VRPApi

All URIs are relative to *https://api.solvice.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_job**](VRPApi.md#get_job) | **GET** /jobs/{jobId} | gets a job
[**get_job_status**](VRPApi.md#get_job_status) | **GET** /jobs/{jobId}/status | gets a job status
[**solve_vrp**](VRPApi.md#solve_vrp) | **POST** /solve#VRP | solve a VRP problem

# **get_job**
> Job get_job(job_id)

gets a job

Retrieve a specific job

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.VRPApi(swagger_client.ApiClient(configuration))
job_id = 'job_id_example' # str | The job ID.

try:
    # gets a job
    api_response = api_instance.get_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VRPApi->get_job: %s\n" % e)
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

# **get_job_status**
> Job get_job_status(job_id)

gets a job status

Retrieve a specific job status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.VRPApi(swagger_client.ApiClient(configuration))
job_id = 'job_id_example' # str | The job ID.

try:
    # gets a job status
    api_response = api_instance.get_job_status(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VRPApi->get_job_status: %s\n" % e)
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

# **solve_vrp**
> Job solve_vrp(body=body)

solve a VRP problem

Adds an item to the system

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.VRPApi(swagger_client.ApiClient(configuration))
body = swagger_client.VRP() # VRP | VRP problem solve request (optional)

try:
    # solve a VRP problem
    api_response = api_instance.solve_vrp(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VRPApi->solve_vrp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VRP**](VRP.md)| VRP problem solve request | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

