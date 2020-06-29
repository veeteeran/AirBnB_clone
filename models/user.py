#!/usr/bin/python3
"""A class for creating users in HolBNB"""
from models import BaseModel


class User(BaseModel):
    """ A class of user for storage of user information """

    def __init__(self, email="", password="", first_naame="", last_name=""):
