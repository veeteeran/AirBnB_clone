#!/usr/bin/python3
"""A class for creating places in HolBNB"""
from models.base_model import BaseModel


class Place(BaseModel):
    """ 
    A class of place information which ties together
    city, state, user, reviews, amenities, as well as
    general information about the place.
    """
    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms =  0
    number_bathrooms =  0
    max_guest =  0
    price_by_night =  0
    latitude = 0.0
    longitude =  0.0
    amenity_ids = ""
