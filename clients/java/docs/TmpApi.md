# TmpApi

All URIs are relative to *https://api.solvice.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getJob**](TmpApi.md#getJob) | **GET** /jobs/{jobId} | Job
[**getJobStatus**](TmpApi.md#getJobStatus) | **GET** /jobs/{jobId}/status | Status
[**solveTMP**](TmpApi.md#solveTMP) | **POST** /solve#TMP | solve a TMP problem

<a name="getJob"></a>
# **getJob**
> Job getJob(jobId)

Job

When posting a new solve request, this job can be checked again under this endpoint. In fact, it should be the entire request posted as-is.

### Example
```java
// Import classes:
//import io.solvice.routing.api.client.ApiClient;
//import io.solvice.routing.api.client.ApiException;
//import io.solvice.routing.api.client.Configuration;
//import io.solvice.routing.api.client.auth.*;
//import io.solvice.routing.api.client.api.TmpApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: basicAuth
HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
basicAuth.setUsername("YOUR USERNAME");
basicAuth.setPassword("YOUR PASSWORD");

TmpApi apiInstance = new TmpApi();
UUID jobId = new UUID(); // UUID | The job ID.
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
 **jobId** | [**UUID**](.md)| The job ID. |

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

Status

Retrieve a specific job status

### Example
```java
// Import classes:
//import io.solvice.routing.api.client.ApiClient;
//import io.solvice.routing.api.client.ApiException;
//import io.solvice.routing.api.client.Configuration;
//import io.solvice.routing.api.client.auth.*;
//import io.solvice.routing.api.client.api.TmpApi;

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
> Job solveTMP(body)

solve a TMP problem

Solves a TMP problem

### Example
```java
// Import classes:
//import io.solvice.routing.api.client.ApiClient;
//import io.solvice.routing.api.client.ApiException;
//import io.solvice.routing.api.client.Configuration;
//import io.solvice.routing.api.client.auth.*;
//import io.solvice.routing.api.client.api.TmpApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: basicAuth
HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
basicAuth.setUsername("YOUR USERNAME");
basicAuth.setPassword("YOUR PASSWORD");

TmpApi apiInstance = new TmpApi();
TMP body = new TMP(); // TMP | TMP problem solve request
try {
    Job result = apiInstance.solveTMP(body);
    System.out.println(result);
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

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

