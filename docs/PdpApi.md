# PdpApi

All URIs are relative to *https://api.solvice.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getJob**](PdpApi.md#getJob) | **GET** /jobs/{jobId} | gets a job
[**getJobStatus**](PdpApi.md#getJobStatus) | **GET** /jobs/{jobId}/status | gets a job status

<a name="getJob"></a>
# **getJob**
> Job getJob(jobId)

gets a job

Retrieve a specific job

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.PdpApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: basicAuth
HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
basicAuth.setUsername("YOUR USERNAME");
basicAuth.setPassword("YOUR PASSWORD");

PdpApi apiInstance = new PdpApi();
String jobId = "jobId_example"; // String | The job ID.
try {
    Job result = apiInstance.getJob(jobId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling PdpApi#getJob");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobId** | **String**| The job ID. |

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="getJobStatus"></a>
# **getJobStatus**
> Job getJobStatus(jobId)

gets a job status

Retrieve a specific job status

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.PdpApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: basicAuth
HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
basicAuth.setUsername("YOUR USERNAME");
basicAuth.setPassword("YOUR PASSWORD");

PdpApi apiInstance = new PdpApi();
String jobId = "jobId_example"; // String | The job ID.
try {
    Job result = apiInstance.getJobStatus(jobId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling PdpApi#getJobStatus");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobId** | **String**| The job ID. |

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

