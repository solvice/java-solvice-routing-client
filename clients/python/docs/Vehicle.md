# Vehicle

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique identification of a vehicle via the name. | 
**startlocation** | **str** | Start address of the vehicle | 
**endlocation** | **str** | End address of the vehicle. The optimisation takes into account the travel back to this location. | [optional] 
**capacity** | **int** | Load capacity of the vehicle. For example, 30 tons is the digit 30. | [optional] 
**capacity2** | **int** | Load capacity of the vehicle (second metric). For example, 400 items. | [optional] 
**shiftstart** | **int** | Starting time of the shift of this vehicle. | [optional] 
**shiftend** | **int** |  | [optional] 
**type** | **list[str]** |  | [optional] 
**unavailable** | **list[date]** |  | [optional] 
**working_days** | **list[str]** |  | [optional] 
**overtime** | **bool** | Indication if vehicle can go in overtime or not. | [optional] 
**overtime_end** | **int** | Last timeblock of overtime. | [optional] 
**breaks** | [**VehicleBreaks**](VehicleBreaks.md) |  | [optional] 
**category** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

