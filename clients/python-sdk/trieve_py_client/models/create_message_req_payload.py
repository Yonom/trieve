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
from typing_extensions import Annotated
from trieve_py_client.models.chunk_filter import ChunkFilter
from trieve_py_client.models.highlight_options import HighlightOptions
from trieve_py_client.models.llm_options import LLMOptions
from trieve_py_client.models.search_method import SearchMethod
from typing import Optional, Set
from typing_extensions import Self

class CreateMessageReqPayload(BaseModel):
    """
    CreateMessageReqPayload
    """ # noqa: E501
    concat_user_messages_query: Optional[StrictBool] = Field(default=None, description="If concat user messages query is set to true, all of the user messages in the topic will be concatenated together and used as the search query. If not specified, this defaults to false. Default is false.")
    filters: Optional[ChunkFilter] = None
    highlight_options: Optional[HighlightOptions] = None
    llm_options: Optional[LLMOptions] = None
    new_message_content: StrictStr = Field(description="The content of the user message to attach to the topic and then generate an assistant message in response to.")
    page_size: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="Page size is the number of chunks to fetch during RAG. If 0, then no search will be performed. If specified, this will override the N retrievals to include in the dataset configuration. Default is None.")
    score_threshold: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Set score_threshold to a float to filter out chunks with a score below the threshold. This threshold applies before weight and bias modifications. If not specified, this defaults to 0.0.")
    search_query: Optional[StrictStr] = Field(default=None, description="Query is the search query. This can be any string. The search_query will be used to create a dense embedding vector and/or sparse vector which will be used to find the result set. If not specified, will default to the last user message or HyDE if HyDE is enabled in the dataset configuration. Default is None.")
    search_type: Optional[SearchMethod] = None
    topic_id: StrictStr = Field(description="The ID of the topic to attach the message to.")
    user_id: Optional[StrictStr] = Field(default=None, description="The user_id is the id of the user who is making the request. This is used to track user interactions with the RAG results.")
    __properties: ClassVar[List[str]] = ["concat_user_messages_query", "filters", "highlight_options", "llm_options", "new_message_content", "page_size", "score_threshold", "search_query", "search_type", "topic_id", "user_id"]

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
        """Create an instance of CreateMessageReqPayload from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of filters
        if self.filters:
            _dict['filters'] = self.filters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of highlight_options
        if self.highlight_options:
            _dict['highlight_options'] = self.highlight_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of llm_options
        if self.llm_options:
            _dict['llm_options'] = self.llm_options.to_dict()
        # set to None if concat_user_messages_query (nullable) is None
        # and model_fields_set contains the field
        if self.concat_user_messages_query is None and "concat_user_messages_query" in self.model_fields_set:
            _dict['concat_user_messages_query'] = None

        # set to None if filters (nullable) is None
        # and model_fields_set contains the field
        if self.filters is None and "filters" in self.model_fields_set:
            _dict['filters'] = None

        # set to None if highlight_options (nullable) is None
        # and model_fields_set contains the field
        if self.highlight_options is None and "highlight_options" in self.model_fields_set:
            _dict['highlight_options'] = None

        # set to None if llm_options (nullable) is None
        # and model_fields_set contains the field
        if self.llm_options is None and "llm_options" in self.model_fields_set:
            _dict['llm_options'] = None

        # set to None if page_size (nullable) is None
        # and model_fields_set contains the field
        if self.page_size is None and "page_size" in self.model_fields_set:
            _dict['page_size'] = None

        # set to None if score_threshold (nullable) is None
        # and model_fields_set contains the field
        if self.score_threshold is None and "score_threshold" in self.model_fields_set:
            _dict['score_threshold'] = None

        # set to None if search_query (nullable) is None
        # and model_fields_set contains the field
        if self.search_query is None and "search_query" in self.model_fields_set:
            _dict['search_query'] = None

        # set to None if search_type (nullable) is None
        # and model_fields_set contains the field
        if self.search_type is None and "search_type" in self.model_fields_set:
            _dict['search_type'] = None

        # set to None if user_id (nullable) is None
        # and model_fields_set contains the field
        if self.user_id is None and "user_id" in self.model_fields_set:
            _dict['user_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateMessageReqPayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "concat_user_messages_query": obj.get("concat_user_messages_query"),
            "filters": ChunkFilter.from_dict(obj["filters"]) if obj.get("filters") is not None else None,
            "highlight_options": HighlightOptions.from_dict(obj["highlight_options"]) if obj.get("highlight_options") is not None else None,
            "llm_options": LLMOptions.from_dict(obj["llm_options"]) if obj.get("llm_options") is not None else None,
            "new_message_content": obj.get("new_message_content"),
            "page_size": obj.get("page_size"),
            "score_threshold": obj.get("score_threshold"),
            "search_query": obj.get("search_query"),
            "search_type": obj.get("search_type"),
            "topic_id": obj.get("topic_id"),
            "user_id": obj.get("user_id")
        })
        return _obj


