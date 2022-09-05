#!/usr/bin/python3

"""Defines the BaseModel class."""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:

    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):

        """Initialize a new BaseModel.

        Args:

            *args (any): Unused.

            **kwargs (dict): Key/value pairs of attributes.

        """

        t_format = "%Y-%m-%dT%H:%M:%S.%f"

        self.id = str(uuid4())

        self.created_at = datetime.now()

        self.updated_at = datetime.now()

        if len(kwargs) != 0:

            for k, v in kwargs.items():

                if k == "created_at" or k == "updated_at":

                    self.__dict__[k] = datetime.strptime(v, t_format)

                else:

                    self.__dict__[k] = v

        else:

            models.storage.new(self)


    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()


    def to_dict(self):

        """Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing

        the class name of the object.

        """

        n_dict = self.__dict__.copy()

        n_dict["created_at"] = self.created_at.isoformat()

        n_dict["updated_at"] = self.updated_at.isoformat()

        n_dict["__class__"] = self.__class__.__name__

        return (n_dict)



    def __str__(self):

        """Return the print/str representation of the BaseModel instance."""

        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
