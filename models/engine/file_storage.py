#!/usr/bin/python3
"""The first file storage engine of HolBnB"""
import json
import os


class FileStorage:
    """ A class to serialize and deserialize JSON and Python Dicts """

    def __init__(self, *args, **kwargs):
        self.__objects = {}
        self.__file_path = os.getcwd() + "/models/engine/json/"

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        Parameters: Takes in an object and adds it to the dictionary __objects
        the key is the obj class+ obj id, the value is the dict of the obj
        """
        return self.__objects.update({str((type(obj).__name__)+'.'+(obj.id)): obj})

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        filename = self.__file_path + 'file.json'
        with open(filename, 'w') as output:
            new_dict = {}
            for k, v in self.__objects.items():
                new_dict.update({k: v.to_dict()})

            json.dump(new_dict, output)

    def reload(self):
        """deserializes the JSON file to __objects if __file_path exists"""
        from models.base_model import BaseModel
        try:
            with open(self.__file_path + 'file.json') as saved_data:
                new_dict = json.load(saved_data)
                for k, v in new_dict.items():
                    new_obj = BaseModel(v)
                    key = str((type(new_obj).__name__)+'.'+(new_obj.id))
                    if key not in self.__objects.keys():
                        self.__objects.update({key: new_obj})
        except:
            pass
