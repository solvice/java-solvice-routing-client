# Options

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile** | **str** | All vehicles are either CAR or TRUCK. | [optional] 
**allow_overtime** | **bool** | If the &#x60;shiftend&#x60; should be a soft condition to take into account. When &#x60;allow_overtime: true&#x60; then some orders will be planned after &#x60;shiftend&#x60;.  | [optional] 
**overconstrained** | **bool** | If you do not need to assign every order to a vehicle, then set &#x60;overconstrained: true&#x60;.  | [optional] 
**minimize_vehicle_use** | **bool** | Minimise the vehicle useage or minimise total travel time. Two different objective functions. | [optional] 
**traffic** | **int** | Modifier for traffic. | [optional] 
**polylines** | **bool** | Let our map server calculate the actual polylines for connecting the visits. Processing will take longer. | [optional] 
**time_unit** | **str** | Calculate in minutes or seconds. Minutes is advised. | [optional] [default to 'MINUTES']
**force_type_constraints** | **bool** | If yes, then the type constraints violations are not allowed. Only do this when you are sure about type definitions. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

