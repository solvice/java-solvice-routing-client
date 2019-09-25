# PvrpApi

All URIs are relative to *https://api.solvice.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**solvePVRP**](PvrpApi.md#solvePVRP) | **POST** /solve#PVRP | Solve a PVRP problem

<a name="solvePVRP"></a>
# **solvePVRP**
> Job solvePVRP(body)

Solve a PVRP problem

Periodic vehicle routing problems

### Example
```java
// Import classes:
//import io.solvice.routing.api.client.ApiClient;
//import io.solvice.routing.api.client.ApiException;
//import io.solvice.routing.api.client.Configuration;
//import io.solvice.routing.api.client.auth.*;
//import io.solvice.routing.api.client.api.PvrpApi;

ApiClient defaultClient = Configuration.getDefaultApiClient();
// Configure HTTP basic authorization: basicAuth
HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
basicAuth.setUsername("YOUR USERNAME");
basicAuth.setPassword("YOUR PASSWORD");

PvrpApi apiInstance = new PvrpApi();
PVRP body = new PVRP(); // PVRP | PVRP problem solve request
try {
    Job result = apiInstance.solvePVRP(body);
    System.out.println(result);
} catch (ApiException e) {
    System.err.println("Exception when calling PvrpApi#solvePVRP");
    e.printStackTrace();
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PVRP**](PVRP.md)| PVRP problem solve request | [optional]

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

