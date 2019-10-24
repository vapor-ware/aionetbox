# CircuitTermination

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**circuit** | [**NestedCircuit**](NestedCircuit.md) |  | 
**term_side** | **str** |  | 
**site** | [**NestedSite**](NestedSite.md) |  | 
**port_speed** | **int** |  | 
**upstream_speed** | **int** | Upstream speed, if different from port speed | [optional] 
**xconnect_id** | **str** |  | [optional] 
**pp_info** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**connected_endpoint_type** | **str** |  | [optional] 
**connected_endpoint** | **dict(str, str)** |          Return the appropriate serializer for the type of connected object.          | [optional] 
**connection_status** | [**ConnectionStatus**](ConnectionStatus.md) |  | [optional] 
**cable** | [**NestedCable**](NestedCable.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


