# coding: utf-8

"""
    Trieve API

    Trieve OpenAPI Specification. This document describes all of the operations available through the Trieve API.

    The version of the OpenAPI document: 0.11.8
    Contact: developers@trieve.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from trieve_py_client.models.sort_by_field import SortByField
from trieve_py_client.models.sort_by_search_type import SortBySearchType
from pydantic import StrictStr, Field
from typing import Union, List, Optional, Dict
from typing_extensions import Literal, Self

QDRANTSORTBY_ONE_OF_SCHEMAS = ["SortByField", "SortBySearchType"]

class QdrantSortBy(BaseModel):
    """
    Sort by lets you specify a method to sort the results by. If not specified, this defaults to the score of the chunks. If specified, this can be any key in the chunk metadata. This key must be a numeric value within the payload.
    """
    # data type: SortByField
    oneof_schema_1_validator: Optional[SortByField] = None
    # data type: SortBySearchType
    oneof_schema_2_validator: Optional[SortBySearchType] = None
    actual_instance: Optional[Union[SortByField, SortBySearchType]] = None
    one_of_schemas: List[str] = Field(default=Literal["SortByField", "SortBySearchType"])

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = QdrantSortBy.model_construct()
        error_messages = []
        match = 0
        # validate data type: SortByField
        if not isinstance(v, SortByField):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SortByField`")
        else:
            match += 1
        # validate data type: SortBySearchType
        if not isinstance(v, SortBySearchType):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SortBySearchType`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in QdrantSortBy with oneOf schemas: SortByField, SortBySearchType. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in QdrantSortBy with oneOf schemas: SortByField, SortBySearchType. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into SortByField
        try:
            instance.actual_instance = SortByField.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SortBySearchType
        try:
            instance.actual_instance = SortBySearchType.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into QdrantSortBy with oneOf schemas: SortByField, SortBySearchType. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into QdrantSortBy with oneOf schemas: SortByField, SortBySearchType. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], SortByField, SortBySearchType]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())

