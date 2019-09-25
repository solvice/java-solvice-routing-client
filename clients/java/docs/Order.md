# Order

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | Unique name of an order | 
**location** | **String** | Location of an order; should be in location list. | 
**activity** | [**ActivityEnum**](#ActivityEnum) | Activity type. When defining a PDP problem, be sure to have both a pickup and a delivery activity for the same ride. See ride. |  [optional]
**ride** | **String** | Only applicable for PDP. Use the same ride string for a pickup and a delivery activity. |  [optional]
**priority** | **Integer** | Priority allows you to make certain visits a priority over others. In some cases you have more visits than you can serve, resulting in a few unserved. But if you want to make sure your high priority visits take precedence, use this parameter and set it to 100.  |  [optional]
**duration** | **Integer** | Duration of the service in minutes |  [optional]
**demand** | **Integer** | Load in cargo for capacity type 1. |  [optional]
**demand2** | **Integer** | Load in cargo for capacity type 2. |  [optional]
**type** | **List&lt;String&gt;** | Type restriction which can force some orders to be executed by Vehicles with the same type. |  [optional]
**windows** | [**List&lt;OrderWindows&gt;**](OrderWindows.md) | A time window consists of a starttime and an endtime. The order cannot be processed before the starttime and should start being processed before endtime. If the time window is hard, then it should always be fulfilled. E.g. a driver would prefer to drive 3 hours longer than not be on time wrt that time window for that order. So hard time window constraints are pretty extreme! |  [optional]
**durationSquash** | **Integer** | When multiple orders are on the same location, the service duration can be lower due to simultaneous handling. The duration will then be this value. is useful when you have many stops at the same location, which could be an apartment complex. Normally, each stop has a duration value of let&#x27;s say 10 minutes, which accounts for parking and finding the entrance. If you had 6 stops assigned to a driver at the same time, it doesn&#x27;t take an hour in total! Use this parameter to squash the durations of each subsequent delivery at the same address. If you set it to 1, it will squash it to 1 minute, so the total duration for the above 6 stops would be 15 minutes. |  [optional]
**dateWindows** | [**List&lt;OrderDateWindows&gt;**](OrderDateWindows.md) | List of start/end date/time combinations. |  [optional]
**allowedVehicles** | **List&lt;String&gt;** | List of vehicle names that are allowed to be assigned to this order |  [optional]
**disallowedVehicles** | **List&lt;String&gt;** | List of vehicle names that are not allowed to be assigned to this order |  [optional]

<a name="ActivityEnum"></a>
## Enum: ActivityEnum
Name | Value
---- | -----
PICKUP | &quot;PICKUP&quot;
DROPOFF | &quot;DROPOFF&quot;
EXECUTE | &quot;EXECUTE&quot;
BREAK | &quot;BREAK&quot;
