# WritableIPAddress

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**family** | **int** |  | [optional] 
**address** | **str** | IPv4 or IPv6 address (with mask) | 
**vrf** | **int** |  | [optional] 
**tenant** | **int** |  | [optional] 
**status** | **int** | The operational status of this IP | [optional] 
**role** | **int** | The functional role of this IP | [optional] 
**interface** | **int** |  | [optional] 
**nat_inside** | **int** | The IP for which this address is the \&quot;outside\&quot; IP | [optional] 
**nat_outside** | **int** |  | 
**dns_name** | **str** | Hostname or FQDN (not case-sensitive) | [optional] 
**description** | **str** |  | [optional] 
**tags** | **list[str]** |  | [optional] 
**custom_fields** | **object** |  | [optional] 
**created** | **date** |  | [optional] 
**last_updated** | **datetime** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


