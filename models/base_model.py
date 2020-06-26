#!/usr/bin python3
""" One base model to rule them all """
import uuid
from datetime import datetime 

class BaseModel:
    """
    The base model from which all classes for this project will inherit
    """
    def __init__(self):
        """
        Init docstring
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        Returns the string format of the object
        """
        return "[BaseModel] ({}) <{}>".format(self.id, self.__dict__)

    def save(self):
        """
        Updates the updated at time to now, to reflect changes
        """
        self.update_at = datetime.now()

    def to_dict(self):
        """
        Builds the dict representation of the object
        """
        self_dict = {
            '__class__': 'BaseModel',
            'id': self.id,
            'created_at': self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
            'upated_at': self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        }
        return self_dict
