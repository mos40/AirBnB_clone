#!/usr/bin/python3
"""Defines the ComfortFeature class."""
from models.base_model import BaseModel


class ComfortFeature(BaseModel):
    """Represents a comfort feature.

    Attributes:
        feature_name (str): The name of the comfort feature.
    """

    feature_name = ""
