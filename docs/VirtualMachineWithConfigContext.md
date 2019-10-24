# VirtualMachineWithConfigContext

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | 
**status** | [**Status**](Status.md) |  | [optional] 
**site** | [**NestedSite**](NestedSite.md) |  | [optional] 
**cluster** | [**NestedCluster**](NestedCluster.md) |  | 
**role** | [**NestedDeviceRole**](NestedDeviceRole.md) |  | [optional] 
**tenant** | [**NestedTenant**](NestedTenant.md) |  | [optional] 
**platform** | [**NestedPlatform**](NestedPlatform.md) |  | [optional] 
**primary_ip** | [**NestedIPAddress**](NestedIPAddress.md) |  | [optional] 
**primary_ip4** | [**NestedIPAddress**](NestedIPAddress.md) |  | [optional] 
**primary_ip6** | [**NestedIPAddress**](NestedIPAddress.md) |  | [optional] 
**vcpus** | **int** |  | [optional] 
**memory** | **int** |  | [optional] 
**disk** | **int** |  | [optional] 
**comments** | **str** |  | [optional] 
**local_context_data** | **str** |  | [optional] 
**tags** | **list[str]** |  | [optional] 
**custom_fields** | **object** |  | [optional] 
**config_context** | **dict(str, str)** |  | [optional] 
**created** | **date** |  | [optional] 
**last_updated** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


