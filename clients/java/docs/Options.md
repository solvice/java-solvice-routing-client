# Options

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | [**ProfileEnum**](#ProfileEnum) |  |  [optional]
**allowOvertime** | **String** | If the &#x60;shiftend&#x60; should be a soft condition to take into account. When &#x60;allow_overtime: true&#x60; then some orders will be planned after &#x60;shiftend&#x60;.  |  [optional]
**overconstrained** | **Boolean** | If you do not need to assign everything to  |  [optional]
**minimizeVehicleUse** | **Boolean** | sd |  [optional]
**vehicleSetupCost** | [**BigDecimal**](BigDecimal.md) |  |  [optional]

<a name="ProfileEnum"></a>
## Enum: ProfileEnum
Name | Value
---- | -----
CAR | &quot;CAR&quot;
TRUCK | &quot;TRUCK&quot;
