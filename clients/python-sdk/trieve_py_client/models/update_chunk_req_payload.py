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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from trieve_py_client.models.full_text_boost import FullTextBoost
from trieve_py_client.models.geo_info import GeoInfo
from trieve_py_client.models.semantic_boost import SemanticBoost
from typing import Optional, Set
from typing_extensions import Self

class UpdateChunkReqPayload(BaseModel):
    """
    UpdateChunkReqPayload
    """ # noqa: E501
    chunk_html: Optional[StrictStr] = Field(default=None, description="HTML content of the chunk you want to update. This can also be plaintext. The innerText of the HTML will be used to create the embedding vector. The point of using HTML is for convienience, as some users have applications where users submit HTML content. If no chunk_html is provided, the existing chunk_html will be used.")
    chunk_id: Optional[StrictStr] = Field(default=None, description="Id of the chunk you want to update. You can provide either the chunk_id or the tracking_id. If both are provided, the chunk_id will be used.")
    convert_html_to_text: Optional[StrictBool] = Field(default=None, description="Convert HTML to raw text before processing to avoid adding noise to the vector embeddings. By default this is true. If you are using HTML content that you want to be included in the vector embeddings, set this to false.")
    fulltext_boost: Optional[FullTextBoost] = None
    group_ids: Optional[List[StrictStr]] = Field(default=None, description="Group ids are the ids of the groups that the chunk should be placed into. This is useful for when you want to update a chunk and add it to a group or multiple groups in one request.")
    group_tracking_ids: Optional[List[StrictStr]] = Field(default=None, description="Group tracking_ids are the tracking_ids of the groups that the chunk should be placed into. This is useful for when you want to update a chunk and add it to a group or multiple groups in one request.")
    image_urls: Optional[List[StrictStr]] = Field(default=None, description="Image urls are a list of urls to images that are associated with the chunk. This is useful for when you want to associate images with a chunk. If no image_urls are provided, the existing image_urls will be used.")
    link: Optional[StrictStr] = Field(default=None, description="Link of the chunk you want to update. This can also be any string. Frequently, this is a link to the source of the chunk. The link value will not affect the embedding creation. If no link is provided, the existing link will be used.")
    location: Optional[GeoInfo] = None
    metadata: Optional[Any] = Field(default=None, description="The metadata is a JSON object which can be used to filter chunks. This is useful for when you want to filter chunks by arbitrary metadata. Unlike with tag filtering, there is a performance hit for filtering on metadata. If no metadata is provided, the existing metadata will be used.")
    num_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Num value is an arbitrary numerical value that can be used to filter chunks. This is useful for when you want to filter chunks by numerical value. If no num_value is provided, the existing num_value will be used.")
    semantic_boost: Optional[SemanticBoost] = None
    tag_set: Optional[List[StrictStr]] = Field(default=None, description="Tag set is a list of tags. This can be used to filter chunks by tag. Unlike with metadata filtering, HNSW indices will exist for each tag such that there is not a performance hit for filtering on them. If no tag_set is provided, the existing tag_set will be used.")
    time_stamp: Optional[StrictStr] = Field(default=None, description="Time_stamp should be an ISO 8601 combined date and time without timezone. It is used for time window filtering and recency-biasing search results. If no time_stamp is provided, the existing time_stamp will be used.")
    tracking_id: Optional[StrictStr] = Field(default=None, description="Tracking_id of the chunk you want to update. This is required to match an existing chunk.")
    weight: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Weight is a float which can be used to bias search results. This is useful for when you want to bias search results for a chunk. The magnitude only matters relative to other chunks in the chunk's dataset dataset. If no weight is provided, the existing weight will be used.")
    __properties: ClassVar[List[str]] = ["chunk_html", "chunk_id", "convert_html_to_text", "fulltext_boost", "group_ids", "group_tracking_ids", "image_urls", "link", "location", "metadata", "num_value", "semantic_boost", "tag_set", "time_stamp", "tracking_id", "weight"]

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
        """Create an instance of UpdateChunkReqPayload from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of fulltext_boost
        if self.fulltext_boost:
            _dict['fulltext_boost'] = self.fulltext_boost.to_dict()
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of semantic_boost
        if self.semantic_boost:
            _dict['semantic_boost'] = self.semantic_boost.to_dict()
        # set to None if chunk_html (nullable) is None
        # and model_fields_set contains the field
        if self.chunk_html is None and "chunk_html" in self.model_fields_set:
            _dict['chunk_html'] = None

        # set to None if chunk_id (nullable) is None
        # and model_fields_set contains the field
        if self.chunk_id is None and "chunk_id" in self.model_fields_set:
            _dict['chunk_id'] = None

        # set to None if convert_html_to_text (nullable) is None
        # and model_fields_set contains the field
        if self.convert_html_to_text is None and "convert_html_to_text" in self.model_fields_set:
            _dict['convert_html_to_text'] = None

        # set to None if fulltext_boost (nullable) is None
        # and model_fields_set contains the field
        if self.fulltext_boost is None and "fulltext_boost" in self.model_fields_set:
            _dict['fulltext_boost'] = None

        # set to None if group_ids (nullable) is None
        # and model_fields_set contains the field
        if self.group_ids is None and "group_ids" in self.model_fields_set:
            _dict['group_ids'] = None

        # set to None if group_tracking_ids (nullable) is None
        # and model_fields_set contains the field
        if self.group_tracking_ids is None and "group_tracking_ids" in self.model_fields_set:
            _dict['group_tracking_ids'] = None

        # set to None if image_urls (nullable) is None
        # and model_fields_set contains the field
        if self.image_urls is None and "image_urls" in self.model_fields_set:
            _dict['image_urls'] = None

        # set to None if link (nullable) is None
        # and model_fields_set contains the field
        if self.link is None and "link" in self.model_fields_set:
            _dict['link'] = None

        # set to None if location (nullable) is None
        # and model_fields_set contains the field
        if self.location is None and "location" in self.model_fields_set:
            _dict['location'] = None

        # set to None if metadata (nullable) is None
        # and model_fields_set contains the field
        if self.metadata is None and "metadata" in self.model_fields_set:
            _dict['metadata'] = None

        # set to None if num_value (nullable) is None
        # and model_fields_set contains the field
        if self.num_value is None and "num_value" in self.model_fields_set:
            _dict['num_value'] = None

        # set to None if semantic_boost (nullable) is None
        # and model_fields_set contains the field
        if self.semantic_boost is None and "semantic_boost" in self.model_fields_set:
            _dict['semantic_boost'] = None

        # set to None if tag_set (nullable) is None
        # and model_fields_set contains the field
        if self.tag_set is None and "tag_set" in self.model_fields_set:
            _dict['tag_set'] = None

        # set to None if time_stamp (nullable) is None
        # and model_fields_set contains the field
        if self.time_stamp is None and "time_stamp" in self.model_fields_set:
            _dict['time_stamp'] = None

        # set to None if tracking_id (nullable) is None
        # and model_fields_set contains the field
        if self.tracking_id is None and "tracking_id" in self.model_fields_set:
            _dict['tracking_id'] = None

        # set to None if weight (nullable) is None
        # and model_fields_set contains the field
        if self.weight is None and "weight" in self.model_fields_set:
            _dict['weight'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateChunkReqPayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "chunk_html": obj.get("chunk_html"),
            "chunk_id": obj.get("chunk_id"),
            "convert_html_to_text": obj.get("convert_html_to_text"),
            "fulltext_boost": FullTextBoost.from_dict(obj["fulltext_boost"]) if obj.get("fulltext_boost") is not None else None,
            "group_ids": obj.get("group_ids"),
            "group_tracking_ids": obj.get("group_tracking_ids"),
            "image_urls": obj.get("image_urls"),
            "link": obj.get("link"),
            "location": GeoInfo.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "metadata": obj.get("metadata"),
            "num_value": obj.get("num_value"),
            "semantic_boost": SemanticBoost.from_dict(obj["semantic_boost"]) if obj.get("semantic_boost") is not None else None,
            "tag_set": obj.get("tag_set"),
            "time_stamp": obj.get("time_stamp"),
            "tracking_id": obj.get("tracking_id"),
            "weight": obj.get("weight")
        })
        return _obj


