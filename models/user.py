#!/usr/bin/python3
"""A class for creating users in HolBNB"""
from models.base_model import BaseModel


class User(BaseModel):
    """ 
    A class of user for storage of user information 
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
