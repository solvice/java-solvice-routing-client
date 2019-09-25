# VrpApi

All URIs are relative to *https://api.solvice.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getJob**](VrpApi.md#getJob) | **GET** /jobs/{jobId} | Job
[**getJobStatus**](VrpApi.md#getJobStatus) | **GET** /jobs/{jobId}/status | Status
[**getSolutionVrp**](VrpApi.md#getSolutionVrp) | **GET** /jobs/{jobId}/solution#VRP | Solution VRP
[**solveVRP**](VrpApi.md#solveVRP) | **POST** /solve#VRP | solve a VRP problem

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
//import io.solvice.routing.api.client.api.VrpApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: basicAuth
HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
basicAuth.setUsername("YOUR USERNAME");
basicAuth.setPassword("YOUR PASSWORD");

VrpApi apiInstance = new VrpApi();
UUID jobId = new UUID(); // UUID | The job ID.
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
//import io.solvice.routing.api.client.api.VrpApi;

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

<a name="getSolutionVrp"></a>
# **getSolutionVrp**
> RoutingSolution getSolutionVrp(jobId)

Solution VRP

Returns the actual solution of the VRP. Only present when the status is &#x60;SOLVED&#x60;.

### Example
```java
// Import classes:
//import io.solvice.routing.api.client.ApiClient;
//import io.solvice.routing.api.client.ApiException;
//import io.solvice.routing.api.client.Configuration;
//import io.solvice.routing.api.client.auth.*;
//import io.solvice.routing.api.client.api.VrpApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: basicAuth
HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
basicAuth.setUsername("YOUR USERNAME");
basicAuth.setPassword("YOUR PASSWORD");

VrpApi apiInstance = new VrpApi();
UUID jobId = new UUID(); // UUID | The job ID.
try {
    RoutingSolution result = apiInstance.getSolutionVrp(jobId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling VrpApi#getSolutionVrp");
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

<a name="solveVRP"></a>
# **solveVRP**
> Job solveVRP(body)

solve a VRP problem

Adds an item to the system

### Example
```java
// Import classes:
//import io.solvice.routing.api.client.ApiClient;
//import io.solvice.routing.api.client.ApiException;
//import io.solvice.routing.api.client.Configuration;
//import io.solvice.routing.api.client.auth.*;
//import io.solvice.routing.api.client.api.VrpApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: basicAuth
HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
basicAuth.setUsername("YOUR USERNAME");
basicAuth.setPassword("YOUR PASSWORD");

VrpApi apiInstance = new VrpApi();
VRP body = new VRP(); // VRP | VRP problem solve request
try {
    Job result = apiInstance.solveVRP(body);
    System.out.println(result);
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

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

