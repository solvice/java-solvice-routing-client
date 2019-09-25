# SolutionApi

All URIs are relative to *https://api.solvice.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSolution**](SolutionApi.md#getSolution) | **GET** /jobs/{jobId}/solution | Solution

<a name="getSolution"></a>
# **getSolution**
> RoutingSolution getSolution(jobId)

Solution

Returns the actual solution of the routing problem. Only present when the status is &#x60;SOLVED&#x60;.

### Example
```java
// Import classes:
//import io.solvice.routing.api.client.ApiClient;
//import io.solvice.routing.api.client.ApiException;
//import io.solvice.routing.api.client.Configuration;
//import io.solvice.routing.api.client.auth.*;
//import io.solvice.routing.api.client.api.SolutionApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: basicAuth
HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
basicAuth.setUsername("YOUR USERNAME");
basicAuth.setPassword("YOUR PASSWORD");

SolutionApi apiInstance = new SolutionApi();
UUID jobId = new UUID(); // UUID | The job ID.
try {
    RoutingSolution result = apiInstance.getSolution(jobId);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling SolutionApi#getSolution");
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

