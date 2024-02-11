#!/usr/bin/python3
"""
Module documentation: Describe the purpose of the module.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    Class documentation: Describe the purpose of the class.
    """
    def __init__(self):
        """
        Method documentation: Describe what this method does.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Method documentation: Describe what this method does.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Method documentation: Describe what this method does.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Method documentation: Describe what this method does.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
