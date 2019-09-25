# SolviceRoutingClient.Api.TMPApi

All URIs are relative to *https://api.solvice.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetJob**](TMPApi.md#getjob) | **GET** /jobs/{jobId} | gets a job
[**GetJobStatus**](TMPApi.md#getjobstatus) | **GET** /jobs/{jobId}/status | gets a job status
[**SolveTMP**](TMPApi.md#solvetmp) | **POST** /solve#TMP | solve a TMP problem

<a name="getjob"></a>
# **GetJob**
> Job GetJob (string jobId)

gets a job

Retrieve a specific job

### Example
```csharp
using System;
using System.Diagnostics;
using SolviceRoutingClient.Api;
using SolviceRoutingClient.Client;
using SolviceRoutingClient.Model;

namespace Example
{
    public class GetJobExample
    {
        public void main()
        {
            // Configure HTTP basic authorization: basicAuth
            Configuration.Default.Username = "YOUR_USERNAME";
            Configuration.Default.Password = "YOUR_PASSWORD";

            var apiInstance = new TMPApi();
            var jobId = jobId_example;  // string | The job ID.

            try
            {
                // gets a job
                Job result = apiInstance.GetJob(jobId);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling TMPApi.GetJob: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobId** | **string**| The job ID. | 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="getjobstatus"></a>
# **GetJobStatus**
> Job GetJobStatus (string jobId)

gets a job status

Retrieve a specific job status

### Example
```csharp
using System;
using System.Diagnostics;
using SolviceRoutingClient.Api;
using SolviceRoutingClient.Client;
using SolviceRoutingClient.Model;

namespace Example
{
    public class GetJobStatusExample
    {
        public void main()
        {
            // Configure HTTP basic authorization: basicAuth
            Configuration.Default.Username = "YOUR_USERNAME";
            Configuration.Default.Password = "YOUR_PASSWORD";

            var apiInstance = new TMPApi();
            var jobId = jobId_example;  // string | The job ID.

            try
            {
                // gets a job status
                Job result = apiInstance.GetJobStatus(jobId);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling TMPApi.GetJobStatus: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobId** | **string**| The job ID. | 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
<a name="solvetmp"></a>
# **SolveTMP**
> void SolveTMP (TMP body = null)

solve a TMP problem

Solves a TMP problem

### Example
```csharp
using System;
using System.Diagnostics;
using SolviceRoutingClient.Api;
using SolviceRoutingClient.Client;
using SolviceRoutingClient.Model;

namespace Example
{
    public class SolveTMPExample
    {
        public void main()
        {
            // Configure HTTP basic authorization: basicAuth
            Configuration.Default.Username = "YOUR_USERNAME";
            Configuration.Default.Password = "YOUR_PASSWORD";

            var apiInstance = new TMPApi();
            var body = new TMP(); // TMP | TMP problem solve request (optional) 

            try
            {
                // solve a TMP problem
                apiInstance.SolveTMP(body);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling TMPApi.SolveTMP: " + e.Message );
            }
        }
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TMP**](TMP.md)| TMP problem solve request | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
