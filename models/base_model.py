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
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Builds the dict representation of the object
        """
        dict_in_box = {'__classname__': self.__class__.__name__}
        for key, value in self.__dict__.items():
            if key == 'created_at':
                time_key = 'created_at'
                time_value = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
                dict_in_box.update({time_key: time_value})
            elif key == 'updated_at':
                time_key = 'updated_at'
                time_value = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
                dict_in_box.update({time_key: time_value})
            else:
                dict_in_box.update({key: value})

        return dict_in_box
