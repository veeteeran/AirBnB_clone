#!/usr/bin/python3
"""A class for creating cities in HolBNB"""
from models.base_model import BaseModel


class City(BaseModel):
    """ 
    A class of city information 
    """
    state_id = ""
    name = ""
