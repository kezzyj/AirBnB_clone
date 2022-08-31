#!/usr/bin/python3

"""
BaseModel Class of Models Module

"""

import os
import json
import models
from uuid import uuid4, UUID
from datetime import datetime


class BaseModel:

    """
        attributes and functions for BaseModel class
    """

def __init__(self, *args, **kwargs):

        """
            instantiation of new BaseModel Class
        """

        if kwargs:

            self.__set_attributes(kwargs)

        else:

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
