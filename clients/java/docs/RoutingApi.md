# RoutingApi

All URIs are relative to *https://api.solvice.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**evaluate**](RoutingApi.md#evaluate) | **POST** /evaluate | Evaluate
[**solve**](RoutingApi.md#solve) | **POST** /solve | Solve

<a name="evaluate"></a>
# **evaluate**
> Object evaluate(body)

Evaluate

Evaluates any problem defined underneath. Result is the job id and its status. Fetch the solution immediately in the response.

### Example
```java
// Import classes:
//import io.solvice.routing.api.client.ApiClient;
//import io.solvice.routing.api.client.ApiException;
//import io.solvice.routing.api.client.Configuration;
//import io.solvice.routing.api.client.auth.*;
//import io.solvice.routing.api.client.api.RoutingApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: basicAuth
HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
basicAuth.setUsername("YOUR USERNAME");
basicAuth.setPassword("YOUR PASSWORD");

RoutingApi apiInstance = new RoutingApi();
Object body = null; // Object | Problem solve request
try {
    Object result = apiInstance.evaluate(body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling RoutingApi#evaluate");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Object**](Object.md)| Problem solve request | [optional]

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="solve"></a>
# **solve**
> Job solve(body)

Solve

Solves any problem defined underneath. Result is the job id and its status. Fetch the solution afterwards in the Solution endpoint.

### Example
```java
// Import classes:
//import io.solvice.routing.api.client.ApiClient;
//import io.solvice.routing.api.client.ApiException;
//import io.solvice.routing.api.client.Configuration;
//import io.solvice.routing.api.client.auth.*;
//import io.solvice.routing.api.client.api.RoutingApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: basicAuth
HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
basicAuth.setUsername("YOUR USERNAME");
basicAuth.setPassword("YOUR PASSWORD");

RoutingApi apiInstance = new RoutingApi();
Object body = null; // Object | Problem solve request
try {
    Job result = apiInstance.solve(body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling RoutingApi#solve");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Object**](Object.md)| Problem solve request | [optional]

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

