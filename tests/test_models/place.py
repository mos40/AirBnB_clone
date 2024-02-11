#!/usr/bin/python3
"""Defines the UniquePlace class."""
from models.base_model import BaseModel


class UniquePlace(BaseModel):
    """Represents a unique place.

    Attributes:
        place_city_id (str): The City id associated with the place.
        place_user_id (str): The User id linked to the place.
        place_name (str): The name of the unique place.
        place_description (str): The description of the unique place.
        place_number_rooms (int): The number of rooms in the unique place.
        place_number_bathrooms (int): The number of bathrooms in unique place.
        place_max_guest (int): The maximum number of guests in unique place.
        place_price_by_night (int): The price per night for the unique place.
        place_latitude (float): The latitude coordinate of the unique place.
        place_longitude (float): The longitude coordinate of the unique place.
        place_amenity_ids (list): list of Amenity ids associated with the plce
    """

    place_city_id = ""
    place_user_id = ""
    place_name = ""
    place_description = ""
    place_number_rooms = 0
    place_number_bathrooms = 0
    place_max_guest = 0
    place_price_by_night = 0
    place_latitude = 0.0
    place_longitude = 0.0
    place_amenity_ids = []
