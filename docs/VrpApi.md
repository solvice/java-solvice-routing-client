# VrpApi

All URIs are relative to *https://api.solvice.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getJob**](VrpApi.md#getJob) | **GET** /jobs/{jobId} | gets a job
[**getJobStatus**](VrpApi.md#getJobStatus) | **GET** /jobs/{jobId}/status | gets a job status
[**solveVRP**](VrpApi.md#solveVRP) | **POST** /solve#VRP | solve a VRP problem

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
//import io.swagger.client.api.VrpApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: basicAuth
HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
basicAuth.setUsername("YOUR USERNAME");
basicAuth.setPassword("YOUR PASSWORD");

VrpApi apiInstance = new VrpApi();
String jobId = "jobId_example"; // String | The job ID.
try {
    Job result = apiInstance.getJob(jobId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling VrpApi#getJob");
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
//import io.swagger.client.api.VrpApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: basicAuth
HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
basicAuth.setUsername("YOUR USERNAME");
basicAuth.setPassword("YOUR PASSWORD");

VrpApi apiInstance = new VrpApi();
String jobId = "jobId_example"; // String | The job ID.
try {
    Job result = apiInstance.getJobStatus(jobId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling VrpApi#getJobStatus");
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

<a name="solveVRP"></a>
# **solveVRP**
> solveVRP(body)

solve a VRP problem

Adds an item to the system

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.VrpApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: basicAuth
HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
basicAuth.setUsername("YOUR USERNAME");
basicAuth.setPassword("YOUR PASSWORD");

VrpApi apiInstance = new VrpApi();
VRP body = new VRP(); // VRP | VRP problem solve request
try {
    apiInstance.solveVRP(body);
} catch (ApiException e) {
    System.err.println("Exception when calling VrpApi#solveVRP");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VRP**](VRP.md)| VRP problem solve request | [optional]

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

