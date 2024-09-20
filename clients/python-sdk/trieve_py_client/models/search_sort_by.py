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
import json
from enum import Enum
from typing_extensions import Self


class SearchSortBy(str, Enum):
    """
    SearchSortBy
    """

    """
    allowed enum values
    """
    CREATED_AT = 'created_at'
    LATENCY = 'latency'
    TOP_SCORE = 'top_score'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SearchSortBy from a JSON string"""
        return cls(json.loads(json_str))


