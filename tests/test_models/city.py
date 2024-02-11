#!/usr/bin/python3
"""Defines the UrbanCenter class."""
from models.base_model import BaseModel


class UrbanCenter(BaseModel):
    """Represents an urban center.

    Attributes:
        urban_state_id (str): The state id associated with the urban center.
        urban_center_name (str): The name of the urban center.
    """

    urban_state_id = ""
    urban_center_name = ""
