# PdpApi

All URIs are relative to *https://api.solvice.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getJob**](PdpApi.md#getJob) | **GET** /jobs/{jobId} | Job
[**getJobStatus**](PdpApi.md#getJobStatus) | **GET** /jobs/{jobId}/status | Status
[**getSolutionPDP**](PdpApi.md#getSolutionPDP) | **GET** /jobs/{jobId}/solution#PDP | Solution PDP
[**solvePDP**](PdpApi.md#solvePDP) | **POST** /solve#PDP | Solve a PDP problem

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
//import io.solvice.routing.api.client.api.PdpApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: basicAuth
HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
basicAuth.setUsername("YOUR USERNAME");
basicAuth.setPassword("YOUR PASSWORD");

PdpApi apiInstance = new PdpApi();
UUID jobId = new UUID(); // UUID | The job ID.
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
//import io.solvice.routing.api.client.api.PdpApi;

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

<a name="getSolutionPDP"></a>
# **getSolutionPDP**
> RoutingSolution getSolutionPDP(jobId)

Solution PDP

Returns the actual solution of the PDP. Only present when the status is &#x60;SOLVED&#x60;.

### Example
```java
// Import classes:
//import io.solvice.routing.api.client.ApiClient;
//import io.solvice.routing.api.client.ApiException;
//import io.solvice.routing.api.client.Configuration;
//import io.solvice.routing.api.client.auth.*;
//import io.solvice.routing.api.client.api.PdpApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: basicAuth
HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
basicAuth.setUsername("YOUR USERNAME");
basicAuth.setPassword("YOUR PASSWORD");

PdpApi apiInstance = new PdpApi();
UUID jobId = new UUID(); // UUID | The job ID.
try {
    RoutingSolution result = apiInstance.getSolutionPDP(jobId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling PdpApi#getSolutionPDP");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobId** | [**UUID**](.md)| The job ID. |

### Return type

[**RoutingSolution**](RoutingSolution.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="solvePDP"></a>
# **solvePDP**
> Job solvePDP(body)

Solve a PDP problem

Pickup and delivery problems

### Example
```java
// Import classes:
//import io.solvice.routing.api.client.ApiClient;
//import io.solvice.routing.api.client.ApiException;
//import io.solvice.routing.api.client.Configuration;
//import io.solvice.routing.api.client.auth.*;
//import io.solvice.routing.api.client.api.PdpApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: basicAuth
HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
basicAuth.setUsername("YOUR USERNAME");
basicAuth.setPassword("YOUR PASSWORD");

PdpApi apiInstance = new PdpApi();
PDP body = new PDP(); // PDP | PDP problem solve request
try {
    Job result = apiInstance.solvePDP(body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling PdpApi#solvePDP");
    e.printStackTrace();
}
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

