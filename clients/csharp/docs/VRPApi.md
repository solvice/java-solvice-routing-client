# SolviceRoutingClient.Api.VRPApi

All URIs are relative to *https://api.solvice.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**GetJob**](VRPApi.md#getjob) | **GET** /jobs/{jobId} | gets a job
[**GetJobStatus**](VRPApi.md#getjobstatus) | **GET** /jobs/{jobId}/status | gets a job status
[**SolveVRP**](VRPApi.md#solvevrp) | **POST** /solve#VRP | solve a VRP problem

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

            var apiInstance = new VRPApi();
            var jobId = jobId_example;  // string | The job ID.

            try
            {
                // gets a job
                Job result = apiInstance.GetJob(jobId);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling VRPApi.GetJob: " + e.Message );
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

            var apiInstance = new VRPApi();
            var jobId = jobId_example;  // string | The job ID.

            try
            {
                // gets a job status
                Job result = apiInstance.GetJobStatus(jobId);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling VRPApi.GetJobStatus: " + e.Message );
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
<a name="solvevrp"></a>
# **SolveVRP**
> Job SolveVRP (VRP body = null)

solve a VRP problem

Adds an item to the system

### Example
```csharp
using System;
using System.Diagnostics;
using SolviceRoutingClient.Api;
using SolviceRoutingClient.Client;
using SolviceRoutingClient.Model;

namespace Example
{
    public class SolveVRPExample
    {
        public void main()
        {
            // Configure HTTP basic authorization: basicAuth
            Configuration.Default.Username = "YOUR_USERNAME";
            Configuration.Default.Password = "YOUR_PASSWORD";

            var apiInstance = new VRPApi();
            var body = new VRP(); // VRP | VRP problem solve request (optional) 

            try
            {
                // solve a VRP problem
                Job result = apiInstance.SolveVRP(body);
                Debug.WriteLine(result);
            }
            catch (Exception e)
            {
                Debug.Print("Exception when calling VRPApi.SolveVRP: " + e.Message );
            }
        }
    }
}
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
