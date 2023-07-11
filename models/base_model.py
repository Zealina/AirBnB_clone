#!/usr/bin/python3
"""
This module contains the 'BaseModel' class that defines common
attributes/methods for other classes in the package
"""
import uuid
from datetime import datetime

class BaseModel:
    """
    The 'BaseModel' class contains all common attributes for other classess
    the attributes are:

        id (str): A unique id for every instance of 'BaseModel'
        created_at (datetime.datetime): The time of creation of instance
        updated_at (datetime.datetime): Last update

    """

    def __init__(self):
        """
        Initialization of an instance
        """
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())

    def __str__(self):
        """
        String representation of the instance of 'BaseModel' class
        """
        cls_name = self.__class__.__name__
        return f"[{cls_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute "updated_at" with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance"""
        inst_dict = self.__dict__
        inst_dict['__class__'] = self.__class__.__name__
        inst_dict['created_at'] = self.created_at.isoformat()
        inst_dict['updated_at'] = self.updated_at.isoformat()
        return inst_dict
