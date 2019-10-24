# WritablePowerOutlet

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**device** | **int** |  | 
**name** | **str** |  | 
**power_port** | **int** |  | [optional] 
**feed_leg** | **int** | Phase (for three-phase feeds) | [optional] 
**description** | **str** |  | [optional] 
**connected_endpoint_type** | **str** |  | [optional] 
**connected_endpoint** | **dict(str, str)** |          Return the appropriate serializer for the type of connected object.          | [optional] 
**connection_status** | **bool** |  | [optional] 
**cable** | [**NestedCable**](NestedCable.md) |  | [optional] 
**tags** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


