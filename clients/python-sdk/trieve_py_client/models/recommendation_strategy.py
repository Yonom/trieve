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


class RecommendationStrategy(str, Enum):
    """
    Strategy to use for recommendations, either \"average_vector\" or \"best_score\". The default is \"average_vector\". The \"average_vector\" strategy will construct a single average vector from the positive and negative samples then use it to perform a pseudo-search. The \"best_score\" strategy is more advanced and navigates the HNSW with a heuristic of picking edges where the point is closer to the positive samples than it is the negatives.
    """

    """
    allowed enum values
    """
    AVERAGE_VECTOR = 'average_vector'
    BEST_SCORE = 'best_score'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RecommendationStrategy from a JSON string"""
        return cls(json.loads(json_str))


