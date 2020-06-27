#!/usr/bin/ptyhon3
"""The first firle storage engine of HolBnB"""
import json
import os


class FileStorage:
    """ A class to serialize and deserialize JSON and Python Dicts """

    def __init__(self, *args, **kwargs):
        self.__objects = {}
        self.__file_path = os.getcwd() + "/models/engine/json/"
        print("The path: " + str(self.__file_path))

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        Parameters: Takes in an object and adds it to the dictionary __objects
        the key is the obj class+ obj id, the value is the dict of the obj
        """
        return self.__objects.update({str((type(obj).__name__)+'.'+(obj.id)): obj.to_dict()})

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        filename = self.__file_path + 'file.json'
        with open(filename, 'w') as output:
            json.dump(self.__objects, output)

    def reload(self):
        """deserializes the JSON file to __objects if __file_path exists"""
        try:
            with open(self.__file_path + 'file.json') as saved_data:
                self.__objects = json.load(saved_data)
        except:
            pass
