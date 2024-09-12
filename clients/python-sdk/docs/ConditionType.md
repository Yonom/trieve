# ConditionType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_range** | [**DateRange**](DateRange.md) |  | [optional] 
**field** | **str** | Field is the name of the field to filter on. The field value will be used to check for an exact substring match on the metadata values for each existing chunk. This is useful for when you want to filter chunks by arbitrary metadata. To access fields inside of the metadata that you provide with the card, prefix the field name with &#x60;metadata.&#x60;. | 
**geo_bounding_box** | [**LocationBoundingBox**](LocationBoundingBox.md) |  | [optional] 
**geo_polygon** | [**LocationPolygon**](LocationPolygon.md) |  | [optional] 
**geo_radius** | [**LocationRadius**](LocationRadius.md) |  | [optional] 
**match_all** | [**List[MatchCondition]**](MatchCondition.md) | Match all lets you pass in an array of values that will return results if all of the items match. The match value will be used to check for an exact substring match on the metadata values for each existing chunk. If both match_all and match_any are provided, the match_any condition will be used. | [optional] 
**match_any** | [**List[MatchCondition]**](MatchCondition.md) | Match any lets you pass in an array of values that will return results if any of the items match. The match value will be used to check for an exact substring match on the metadata values for each existing chunk. If both match_all and match_any are provided, the match_any condition will be used. | [optional] 
**range** | [**Range**](Range.md) |  | [optional] 
**ids** | **List[str]** |  | [optional] 
**tracking_ids** | **List[str]** |  | [optional] 

## Example

```python
from trieve_py_client.models.condition_type import ConditionType

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionType from a JSON string
condition_type_instance = ConditionType.from_json(json)
# print the JSON string representation of the object
print(ConditionType.to_json())

# convert the object into a dict
condition_type_dict = condition_type_instance.to_dict()
# create an instance of ConditionType from a dict
condition_type_form_dict = condition_type.from_dict(condition_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

