#!/usr/bin/python3

"""
BaseModel Class of Models Module

"""

import os
import json
import models
from uuid import uuid4, UUID
from datetime import datetime

date_format = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:

    """
        attributes and functions for BaseModel class
    """

def __init__(self, *args, **kwargs):

        """
            instantiation of new BaseModel Class
        """

        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

def save(self):
    """
        updates attribute updated_at to current time
    """

    self.updated_at = datetime.utcnow()

def __str__(self):

        """

            returns string type representation of object instance

        """

        class_name = type(self).__name__
        return '[{}] ({}) {}'.format(class_name, self.id, self.__dict__)

def to_dict(self):
     """
       return a dictionary containing all the key/value 
       of __dict__ instance

    """
    new_dict = self.__dict__.copy()
    new_dict["__class__"] = self.__class__.name
    new_dict["created_at"] = datetime.isoformat(self.created_at)
    new_dict["updated_at"] = datetime.isoformat(self.updated_at)
    return new_dict
