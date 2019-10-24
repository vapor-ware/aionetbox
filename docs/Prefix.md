# Prefix

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**family** | [**Status**](Status.md) |  | [optional] 
**prefix** | **str** | IPv4 or IPv6 network with mask | 
**site** | [**NestedSite**](NestedSite.md) |  | [optional] 
**vrf** | [**NestedVRF**](NestedVRF.md) |  | [optional] 
**tenant** | [**NestedTenant**](NestedTenant.md) |  | [optional] 
**vlan** | [**NestedVLAN**](NestedVLAN.md) |  | [optional] 
**status** | [**Status**](Status.md) |  | [optional] 
**role** | [**NestedRole**](NestedRole.md) |  | [optional] 
**is_pool** | **bool** | All IP addresses within this prefix are considered usable | [optional] 
**description** | **str** |  | [optional] 
**tags** | **list[str]** |  | [optional] 
**custom_fields** | **object** |  | [optional] 
**created** | **date** |  | [optional] 
**last_updated** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


