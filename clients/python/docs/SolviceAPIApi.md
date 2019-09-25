# SolviceRoutingClient.SolviceAPIApi

All URIs are relative to *https://api.solvice.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_job**](SolviceAPIApi.md#get_job) | **GET** /jobs/{jobId} | Job
[**get_job_status**](SolviceAPIApi.md#get_job_status) | **GET** /jobs/{jobId}/status | Status
[**get_solution**](SolviceAPIApi.md#get_solution) | **GET** /jobs/{jobId}/solution | Solution
[**get_stats**](SolviceAPIApi.md#get_stats) | **GET** /v1/stats/{jobId} | Statistics

# **get_job**
> Job get_job(job_id)

Job

When posting a new solve request, this job can be checked again under this endpoint. In fact, it should be the entire request posted as-is.

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
api_instance = SolviceRoutingClient.SolviceAPIApi(SolviceRoutingClient.ApiClient(configuration))
job_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The job ID.

try:
    # Job
    api_response = api_instance.get_job(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SolviceAPIApi->get_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | [**str**](.md)| The job ID. | 

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
api_instance = SolviceRoutingClient.SolviceAPIApi(SolviceRoutingClient.ApiClient(configuration))
job_id = 'job_id_example' # str | The job ID.

try:
    # Status
    api_response = api_instance.get_job_status(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SolviceAPIApi->get_job_status: %s\n" % e)
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

# **get_solution**
> Job get_solution(job_id)

Solution

Returns the actual solution of the job. Only present when the status is `SOLVED`.

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
api_instance = SolviceRoutingClient.SolviceAPIApi(SolviceRoutingClient.ApiClient(configuration))
job_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The job ID.

try:
    # Solution
    api_response = api_instance.get_solution(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SolviceAPIApi->get_solution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | [**str**](.md)| The job ID. | 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stats**
> Stats get_stats(job_id)

Statistics

Returns the information on why a job has been solved the way it's been. Information includes specific unresolved objects. Want to know how it is optimised? This endpoint lets you know what rules have been overruled. 

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
api_instance = SolviceRoutingClient.SolviceAPIApi(SolviceRoutingClient.ApiClient(configuration))
job_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The job ID.

try:
    # Statistics
    api_response = api_instance.get_stats(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SolviceAPIApi->get_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | [**str**](.md)| The job ID. | 

### Return type

[**Stats**](Stats.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

