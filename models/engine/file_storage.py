#!/usr/bin/python3
"""
This module contains 'FileStorage' class that serializes and deserializes JSON file to instances
"""

class FileStorage:
    """
    This class serializes instances to a json file and deserializes json file to
    instances. 'FileStorage' has the following class attributes:
        __file_path (str): path to the JSON file
        __objects (dict): ditionary containing objects
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """
        Initializes an instance of 'FileStorage'
        """
        pass

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in '__objects' the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, 'r+', encoding='utf-8') as f:
            json.dump(FileStorage.__objects, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                FileStorage.__objects = json.load(f)
        except FileNotFoundError:
            pass
