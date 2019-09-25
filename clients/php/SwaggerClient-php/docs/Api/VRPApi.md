# Swagger\Client\VRPApi

All URIs are relative to *https://api.solvice.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getJob**](VRPApi.md#getJob) | **GET** /jobs/{jobId} | gets a job
[**getJobStatus**](VRPApi.md#getJobStatus) | **GET** /jobs/{jobId}/status | gets a job status
[**solveVRP**](VRPApi.md#solveVRP) | **POST** /solve#VRP | solve a VRP problem

# **getJob**
> \Swagger\Client\Model\Job getJob($job_id)

gets a job

Retrieve a specific job

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
// Configure HTTP basic authorization: basicAuth
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\routing-client\VRPApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$job_id = "job_id_example"; // string | The job ID.

try {
    $result = $apiInstance->getJob($job_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling VRPApi->getJob: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **string**| The job ID. |

### Return type

[**\Swagger\Client\Model\Job**](../Model/Job.md)

### Authorization

[basicAuth](../../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **getJobStatus**
> \Swagger\Client\Model\Job getJobStatus($job_id)

gets a job status

Retrieve a specific job status

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
// Configure HTTP basic authorization: basicAuth
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\routing-client\VRPApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$job_id = "job_id_example"; // string | The job ID.

try {
    $result = $apiInstance->getJobStatus($job_id);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling VRPApi->getJobStatus: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **string**| The job ID. |

### Return type

[**\Swagger\Client\Model\Job**](../Model/Job.md)

### Authorization

[basicAuth](../../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

# **solveVRP**
> \Swagger\Client\Model\Job solveVRP($body)

solve a VRP problem

Adds an item to the system

### Example
```php
<?php
require_once(__DIR__ . '/vendor/autoload.php');
// Configure HTTP basic authorization: basicAuth
$config = Swagger\Client\Configuration::getDefaultConfiguration()
              ->setUsername('YOUR_USERNAME')
              ->setPassword('YOUR_PASSWORD');


$apiInstance = new Swagger\Client\routing-client\VRPApi(
    // If you want use custom http client, pass your client which implements `GuzzleHttp\ClientInterface`.
    // This is optional, `GuzzleHttp\Client` will be used as default.
    new GuzzleHttp\Client(),
    $config
);
$body = new \Swagger\Client\Model\VRP(); // \Swagger\Client\Model\VRP | VRP problem solve request

try {
    $result = $apiInstance->solveVRP($body);
    print_r($result);
} catch (Exception $e) {
    echo 'Exception when calling VRPApi->solveVRP: ', $e->getMessage(), PHP_EOL;
}
?>
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**\Swagger\Client\Model\VRP**](../Model/VRP.md)| VRP problem solve request | [optional]

### Return type

[**\Swagger\Client\Model\Job**](../Model/Job.md)

### Authorization

[basicAuth](../../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../README.md#documentation-for-models) [[Back to README]](../../README.md)

