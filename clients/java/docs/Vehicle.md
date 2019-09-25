# Vehicle

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | Unique identification of a vehicle via the name. | 
**startlocation** | **String** | Start address of the vehicle | 
**endlocation** | **String** | End address of the vehicle. The optimisation takes into account the travel back to this location. |  [optional]
**capacity** | **Integer** | Load capacity of the vehicle. For example, 30 tons is the digit 30. |  [optional]
**capacity2** | **Integer** | Load capacity of the vehicle (second metric). For example, 400 items. |  [optional]
**shiftstart** | **Integer** | Starting time of the shift of this vehicle. |  [optional]
**shiftend** | **Integer** |  |  [optional]
**type** | **List&lt;String&gt;** |  |  [optional]
**unavailable** | [**List&lt;LocalDate&gt;**](LocalDate.md) |  |  [optional]
**workingDays** | **List&lt;String&gt;** |  |  [optional]
**overtime** | **Boolean** | Indication if vehicle can go in overtime or not. |  [optional]
**overtimeEnd** | **Integer** | Last timeblock of overtime. |  [optional]
**breaks** | [**VehicleBreaks**](VehicleBreaks.md) |  |  [optional]
**category** | [**CategoryEnum**](#CategoryEnum) |  |  [optional]

<a name="CategoryEnum"></a>
## Enum: CategoryEnum
Name | Value
---- | -----
CAR | &quot;CAR&quot;
BIKE | &quot;BIKE&quot;
TRUCK | &quot;TRUCK&quot;
