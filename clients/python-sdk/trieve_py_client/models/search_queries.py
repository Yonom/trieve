# coding: utf-8

"""
    Trieve API

    Trieve OpenAPI Specification. This document describes all of the operations available through the Trieve API.

    The version of the OpenAPI document: 0.11.9
    Contact: developers@trieve.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from trieve_py_client.models.search_analytics_filter import SearchAnalyticsFilter
from trieve_py_client.models.search_sort_by import SearchSortBy
from trieve_py_client.models.sort_order import SortOrder
from typing import Optional, Set
from typing_extensions import Self

class SearchQueries(BaseModel):
    """
    SearchQueries
    """ # noqa: E501
    filter: Optional[SearchAnalyticsFilter] = None
    page: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    sort_by: Optional[SearchSortBy] = None
    sort_order: Optional[SortOrder] = None
    type: StrictStr
    __properties: ClassVar[List[str]] = ["filter", "page", "sort_by", "sort_order", "type"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['search_queries']):
            raise ValueError("must be one of enum values ('search_queries')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SearchQueries from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of filter
        if self.filter:
            _dict['filter'] = self.filter.to_dict()
        # set to None if filter (nullable) is None
        # and model_fields_set contains the field
        if self.filter is None and "filter" in self.model_fields_set:
            _dict['filter'] = None

        # set to None if page (nullable) is None
        # and model_fields_set contains the field
        if self.page is None and "page" in self.model_fields_set:
            _dict['page'] = None

        # set to None if sort_by (nullable) is None
        # and model_fields_set contains the field
        if self.sort_by is None and "sort_by" in self.model_fields_set:
            _dict['sort_by'] = None

        # set to None if sort_order (nullable) is None
        # and model_fields_set contains the field
        if self.sort_order is None and "sort_order" in self.model_fields_set:
            _dict['sort_order'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SearchQueries from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "filter": SearchAnalyticsFilter.from_dict(obj["filter"]) if obj.get("filter") is not None else None,
            "page": obj.get("page"),
            "sort_by": obj.get("sort_by"),
            "sort_order": obj.get("sort_order"),
            "type": obj.get("type")
        })
        return _obj


