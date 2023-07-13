#!/usr/bin/python3
"""
The module contains the User class that defines the attributes of the user
"""

from models.base_model import BaseModel

class User(BaseModel):
    """
    Defines the attributes of the user and methods to manipulate
    said attributes
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
