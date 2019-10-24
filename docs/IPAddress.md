# IPAddress

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**family** | [**Status**](Status.md) |  | [optional] 
**address** | **str** | IPv4 or IPv6 address (with mask) | 
**vrf** | [**NestedVRF**](NestedVRF.md) |  | [optional] 
**tenant** | [**NestedTenant**](NestedTenant.md) |  | [optional] 
**status** | [**Status**](Status.md) |  | [optional] 
**role** | [**Status**](Status.md) |  | [optional] 
**interface** | [**IPAddressInterface**](IPAddressInterface.md) |  | [optional] 
**nat_inside** | [**NestedIPAddress**](NestedIPAddress.md) |  | [optional] 
**nat_outside** | [**NestedIPAddress**](NestedIPAddress.md) |  | [optional] 
**dns_name** | **str** | Hostname or FQDN (not case-sensitive) | [optional] 
**description** | **str** |  | [optional] 
**tags** | **list[str]** |  | [optional] 
**custom_fields** | **object** |  | [optional] 
**created** | **date** |  | [optional] 
**last_updated** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


