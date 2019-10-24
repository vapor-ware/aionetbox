# PowerPort

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**device** | [**NestedDevice**](NestedDevice.md) |  | 
**name** | **str** |  | 
**maximum_draw** | **int** | Maximum current draw (watts) | [optional] 
**allocated_draw** | **int** | Allocated current draw (watts) | [optional] 
**description** | **str** |  | [optional] 
**connected_endpoint_type** | **str** |  | [optional] 
**connected_endpoint** | **dict(str, str)** |          Return the appropriate serializer for the type of connected object.          | [optional] 
**connection_status** | [**ConnectionStatus**](ConnectionStatus.md) |  | [optional] 
**cable** | [**NestedCable**](NestedCable.md) |  | [optional] 
**tags** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


