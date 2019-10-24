# WritableDeviceWithConfigContext

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**device_type** | **int** |  | 
**device_role** | **int** |  | 
**tenant** | **int** |  | [optional] 
**platform** | **int** |  | [optional] 
**serial** | **str** |  | [optional] 
**asset_tag** | **str** | A unique tag used to identify this device | [optional] 
**site** | **int** |  | 
**rack** | **int** |  | [optional] 
**position** | **int** | The lowest-numbered unit occupied by the device | [optional] 
**face** | **int** |  | [optional] 
**parent_device** | [**NestedDevice**](NestedDevice.md) |  | [optional] 
**status** | **int** |  | [optional] 
**primary_ip** | **str** |  | [optional] 
**primary_ip4** | **int** |  | [optional] 
**primary_ip6** | **int** |  | [optional] 
**cluster** | **int** |  | [optional] 
**virtual_chassis** | **int** |  | [optional] 
**vc_position** | **int** |  | [optional] 
**vc_priority** | **int** |  | [optional] 
**comments** | **str** |  | [optional] 
**local_context_data** | **str** |  | [optional] 
**tags** | **list[str]** |  | [optional] 
**custom_fields** | **object** |  | [optional] 
**config_context** | **dict(str, str)** |  | [optional] 
**created** | **date** |  | [optional] 
**last_updated** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


