# SolviceApiApi

All URIs are relative to *https://api.solvice.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getJob**](SolviceApiApi.md#getJob) | **GET** /jobs/{jobId} | Job
[**getJobStatus**](SolviceApiApi.md#getJobStatus) | **GET** /jobs/{jobId}/status | Status
[**getSolution**](SolviceApiApi.md#getSolution) | **GET** /jobs/{jobId}/solution | Solution
[**getStats**](SolviceApiApi.md#getStats) | **GET** /v1/stats/{jobId} | Statistics

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
//import io.solvice.routing.api.client.api.SolviceApiApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: basicAuth
HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
basicAuth.setUsername("YOUR USERNAME");
basicAuth.setPassword("YOUR PASSWORD");

SolviceApiApi apiInstance = new SolviceApiApi();
UUID jobId = new UUID(); // UUID | The job ID.
try {
    Job result = apiInstance.getJob(jobId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling SolviceApiApi#getJob");
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
//import io.solvice.routing.api.client.api.SolviceApiApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: basicAuth
HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
basicAuth.setUsername("YOUR USERNAME");
basicAuth.setPassword("YOUR PASSWORD");

SolviceApiApi apiInstance = new SolviceApiApi();
String jobId = "jobId_example"; // String | The job ID.
try {
    Job result = apiInstance.getJobStatus(jobId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling SolviceApiApi#getJobStatus");
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

<a name="getSolution"></a>
# **getSolution**
> Job getSolution(jobId)

Solution

Returns the actual solution of the job. Only present when the status is &#x60;SOLVED&#x60;.

### Example
```java
// Import classes:
//import io.solvice.routing.api.client.ApiClient;
//import io.solvice.routing.api.client.ApiException;
//import io.solvice.routing.api.client.Configuration;
//import io.solvice.routing.api.client.auth.*;
//import io.solvice.routing.api.client.api.SolviceApiApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: basicAuth
HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
basicAuth.setUsername("YOUR USERNAME");
basicAuth.setPassword("YOUR PASSWORD");

SolviceApiApi apiInstance = new SolviceApiApi();
UUID jobId = new UUID(); // UUID | The job ID.
try {
    Job result = apiInstance.getSolution(jobId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling SolviceApiApi#getSolution");
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

<a name="getStats"></a>
# **getStats**
> Stats getStats(jobId)

Statistics

Returns the information on why a job has been solved the way it&#x27;s been. Information includes specific unresolved objects. Want to know how it is optimised? This endpoint lets you know what rules have been overruled. 

### Example
```java
// Import classes:
//import io.solvice.routing.api.client.ApiClient;
//import io.solvice.routing.api.client.ApiException;
//import io.solvice.routing.api.client.Configuration;
//import io.solvice.routing.api.client.auth.*;
//import io.solvice.routing.api.client.api.SolviceApiApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: basicAuth
HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
basicAuth.setUsername("YOUR USERNAME");
basicAuth.setPassword("YOUR PASSWORD");

SolviceApiApi apiInstance = new SolviceApiApi();
UUID jobId = new UUID(); // UUID | The job ID.
try {
    Stats result = apiInstance.getStats(jobId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling SolviceApiApi#getStats");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobId** | [**UUID**](.md)| The job ID. |

### Return type

[**Stats**](Stats.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

