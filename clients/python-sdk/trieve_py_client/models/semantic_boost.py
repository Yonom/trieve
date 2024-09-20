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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Union
from typing import Optional, Set
from typing_extensions import Self

class SemanticBoost(BaseModel):
    """
    Distance phrase is useful for moving the embedding vector of the chunk in the direction of the distance phrase. I.e. you can push a chunk with a chunk_html of \"iphone\" 25% closer to the term \"flagship\" by using the distance phrase \"flagship\" and a distance factor of 0.25. Conceptually it's drawing a line (euclidean/L2 distance) between the vector for the innerText of the chunk_html and distance_phrase then moving the vector of the chunk_html distance_factor*L2Distance closer to or away from the distance_phrase point along the line between the two points.
    """ # noqa: E501
    distance_factor: Union[StrictFloat, StrictInt] = Field(description="Arbitrary float (positive or negative) specifying the multiplicate factor to apply before summing the phrase vector with the chunk_html embedding vector")
    phrase: StrictStr = Field(description="Terms to embed in order to create the vector which is weighted summed with the chunk_html embedding vector")
    __properties: ClassVar[List[str]] = ["distance_factor", "phrase"]

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
        """Create an instance of SemanticBoost from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SemanticBoost from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "distance_factor": obj.get("distance_factor"),
            "phrase": obj.get("phrase")
        })
        return _obj


