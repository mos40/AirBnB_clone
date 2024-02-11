#!/usr/bin/python3
"""Defines the ReviewData class."""
from models.base_model import BaseModel


class ReviewData(BaseModel):
    """Represents review data.

    Attributes:
        review_place_id (str): The Place id of the review.
        review_user_id (str): The User id associated with the review.
        review_text (str): The text content of the review.
    """

    review_place_id = ""
    review_user_id = ""
    review_text = ""
