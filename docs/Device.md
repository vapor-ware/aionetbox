# Device

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**device_type** | [**NestedDeviceType**](NestedDeviceType.md) |  | 
**device_role** | [**NestedDeviceRole**](NestedDeviceRole.md) |  | 
**tenant** | [**NestedTenant**](NestedTenant.md) |  | [optional] 
**platform** | [**NestedPlatform**](NestedPlatform.md) |  | [optional] 
**serial** | **str** |  | [optional] 
**asset_tag** | **str** | A unique tag used to identify this device | [optional] 
**site** | [**NestedSite**](NestedSite.md) |  | 
**rack** | [**NestedRack**](NestedRack.md) |  | [optional] 
**position** | **int** | The lowest-numbered unit occupied by the device | [optional] 
**face** | [**Face**](Face.md) |  | [optional] 
**parent_device** | [**NestedDevice**](NestedDevice.md) |  | [optional] 
**status** | [**Status**](Status.md) |  | [optional] 
**primary_ip** | [**NestedIPAddress**](NestedIPAddress.md) |  | [optional] 
**primary_ip4** | [**NestedIPAddress**](NestedIPAddress.md) |  | [optional] 
**primary_ip6** | [**NestedIPAddress**](NestedIPAddress.md) |  | [optional] 
**cluster** | [**NestedCluster**](NestedCluster.md) |  | [optional] 
**virtual_chassis** | [**NestedVirtualChassis**](NestedVirtualChassis.md) |  | [optional] 
**vc_position** | **int** |  | [optional] 
**vc_priority** | **int** |  | [optional] 
**comments** | **str** |  | [optional] 
**local_context_data** | **str** |  | [optional] 
**tags** | **list[str]** |  | [optional] 
**custom_fields** | **object** |  | [optional] 
**created** | **date** |  | [optional] 
**last_updated** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


