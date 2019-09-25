# TmpApi

All URIs are relative to *https://api.solvice.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getJob**](TmpApi.md#getJob) | **GET** /jobs/{jobId} | gets a job
[**getJobStatus**](TmpApi.md#getJobStatus) | **GET** /jobs/{jobId}/status | gets a job status
[**solveTMP**](TmpApi.md#solveTMP) | **POST** /solve#TMP | solve a TMP problem

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
//import io.swagger.client.api.TmpApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: basicAuth
HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
basicAuth.setUsername("YOUR USERNAME");
basicAuth.setPassword("YOUR PASSWORD");

TmpApi apiInstance = new TmpApi();
String jobId = "jobId_example"; // String | The job ID.
try {
    Job result = apiInstance.getJob(jobId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling TmpApi#getJob");
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
//import io.swagger.client.api.TmpApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: basicAuth
HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
basicAuth.setUsername("YOUR USERNAME");
basicAuth.setPassword("YOUR PASSWORD");

TmpApi apiInstance = new TmpApi();
String jobId = "jobId_example"; // String | The job ID.
try {
    Job result = apiInstance.getJobStatus(jobId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling TmpApi#getJobStatus");
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

<a name="solveTMP"></a>
# **solveTMP**
> solveTMP(body)

solve a TMP problem

Solves a TMP problem

### Example
```java
// Import classes:
//import io.swagger.client.ApiClient;
//import io.swagger.client.ApiException;
//import io.swagger.client.Configuration;
//import io.swagger.client.auth.*;
//import io.swagger.client.api.TmpApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: basicAuth
HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
basicAuth.setUsername("YOUR USERNAME");
basicAuth.setPassword("YOUR PASSWORD");

TmpApi apiInstance = new TmpApi();
TMP body = new TMP(); // TMP | TMP problem solve request
try {
    apiInstance.solveTMP(body);
} catch (ApiException e) {
    System.err.println("Exception when calling TmpApi#solveTMP");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TMP**](TMP.md)| TMP problem solve request | [optional]

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

