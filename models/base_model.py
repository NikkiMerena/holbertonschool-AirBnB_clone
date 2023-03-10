#!/usr/bin/python3
"""
Class BaseModel that defines all common
attributes/methods for other classes.
"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """
    Class BaseModel that defines all common
    attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Instanitation
        """
        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.fromisoformat(value)
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Prints: [<class name>] (<self.id>) <self.__dict__>
        """

        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing
        all keys/values of __dict__ of the instance
        """

def to_dict(self):
    """Dictionary of key/values"""
    obj_dict = self.__dict__.copy()
    obj_dict['__class__'] = self.__class__.__name__
    obj_dict['created_at'] = self.created_at.isoformat()
    obj_dict['updated_at'] = self.updated_at.isoformat()
    return obj_dict
