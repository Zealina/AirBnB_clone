#!/usr/bin/python3
"""
This module contains 'FileStorage' class that serializes and deserializes
JSON file to instances
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.place import Place


class FileStorage:
    """
    This class serializes instances to a json file and deserializes json
    file to instances. 'FileStorage' has the following class attributes:
        __file_path (str): path to the JSON file
        __objects (dict): ditionary containing objects
    """
    __file_path = "file.json"
    __objects = {}
    class_dict = {
            "BaseModel": BaseModel, "User": User,
            "State": State, "Amenity": Amenity,
            "Review": Review, "Place": Place
    }

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in '__objects' the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        tbd = {}
        for key in self.__objects.keys():
            obj = self.__objects[key]
            obj = obj.to_dict()
            tbd[key] = obj
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(tbd, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            for key, value in data.items():
                inst = self.class_dict[value['__class__']](**value)
                self.__objects[key] = inst
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            pass
