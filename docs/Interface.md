# Interface

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**device** | [**NestedDevice**](NestedDevice.md) |  | 
**name** | **str** |  | 
**type** | [**Status**](Status.md) |  | [optional] 
**form_factor** | [**Status**](Status.md) |  | [optional] 
**enabled** | **bool** |  | [optional] 
**lag** | [**NestedInterface**](NestedInterface.md) |  | [optional] 
**mtu** | **int** |  | [optional] 
**mac_address** | **str** |  | [optional] 
**mgmt_only** | **bool** | This interface is used only for out-of-band management | [optional] 
**description** | **str** |  | [optional] 
**connected_endpoint_type** | **str** |  | [optional] 
**connected_endpoint** | **dict(str, str)** |          Return the appropriate serializer for the type of connected object.          | [optional] 
**connection_status** | [**ConnectionStatus**](ConnectionStatus.md) |  | [optional] 
**cable** | [**NestedCable**](NestedCable.md) |  | [optional] 
**mode** | [**Status**](Status.md) |  | [optional] 
**untagged_vlan** | [**NestedVLAN**](NestedVLAN.md) |  | [optional] 
**tagged_vlans** | [**list[NestedVLAN]**](NestedVLAN.md) |  | [optional] 
**tags** | **list[str]** |  | [optional] 
**count_ipaddresses** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


