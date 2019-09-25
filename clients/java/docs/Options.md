# Options

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**ProfileEnum**](#ProfileEnum) | All vehicles are either CAR or TRUCK. |  [optional]
**allowOvertime** | **Boolean** | If the &#x60;shiftend&#x60; should be a soft condition to take into account. When &#x60;allow_overtime: true&#x60; then some orders will be planned after &#x60;shiftend&#x60;.  |  [optional]
**overconstrained** | **Boolean** | If you do not need to assign every order to a vehicle, then set &#x60;overconstrained: true&#x60;.  |  [optional]
**minimizeVehicleUse** | **Boolean** | Minimise the vehicle useage or minimise total travel time. Two different objective functions. |  [optional]
**traffic** | **Integer** | Modifier for traffic. |  [optional]
**polylines** | **Boolean** | Let our map server calculate the actual polylines for connecting the visits. Processing will take longer. |  [optional]
**timeUnit** | [**TimeUnitEnum**](#TimeUnitEnum) | Calculate in minutes or seconds. Minutes is advised. |  [optional]
**forceTypeConstraints** | **Boolean** | If yes, then the type constraints violations are not allowed. Only do this when you are sure about type definitions. |  [optional]

<a name="ProfileEnum"></a>
## Enum: ProfileEnum
Name | Value
---- | -----
CAR | &quot;CAR&quot;
TRUCK | &quot;TRUCK&quot;

<a name="TimeUnitEnum"></a>
## Enum: TimeUnitEnum
Name | Value
---- | -----
MINUTES | &quot;MINUTES&quot;
SECONDS | &quot;SECONDS&quot;
