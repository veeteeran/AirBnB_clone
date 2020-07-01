#!/usr/bin/python3
"""The first file storage engine of HolBnB"""
import json
import os


class FileStorage:
    """ A class to serialize and deserialize JSON and Python Dicts """

    __objects = {}
    __file_path = "file.json"

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        Parameters: Takes in an object and adds it to the dictionary __objects
        the key is the obj class+ obj id, the value is the dict of the obj
        """
        key = str((type(obj).__name__) + '.' + (obj.id))
        return self.__objects.update({key: obj})

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        filename = self.__file_path
        with open(filename, 'w') as output:
            new_dict = {}
            for k, v in self.__objects.items():
                new_dict.update({k: v.to_dict()})

            json.dump(new_dict, output)

    def reload(self):
        """deserializes the JSON file to __objects if __file_path exists"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {"BaseModel": BaseModel, "User": User,
                   "Place": Place, "State": State,
                   "City": City, "Amenity": Amenity,
                   "Review": Review}
        try:
            with open(self.__file_path) as saved_data:
                new_dict = json.load(saved_data)
                for k, v in new_dict.items():
                    for key in classes.keys():
                        if str(new_dict[k]['__class__']) == key:
                            new_obj = classes[key](**v)
                            key = str((type(new_obj).__name__) + '.' +
                                      (new_obj.id))
                            self.__objects.update({key: new_obj})
        except:
            print("Something went wrong somewhere,\
            this is from reload, Good Luck!")
