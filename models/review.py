#!/usr/bin/python3
"""A class for creating reviews in HolBNB"""
from models.base_model import BaseModel


class User(BaseModel):
    """ 
    A class of review information for units in HolBnb 
    """
    place_id = ""
    user_id = ""
    text = ""
