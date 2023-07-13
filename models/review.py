#!/usr/bin/python3
"""
This Module contains the class 'Review'
"""

from models.base_model import BaseModel

class Review(BaseModel):
    """
    Contains all class attributes for 'Review'
    """
    place_id = ''
    user_id = ''
    text  = ''
