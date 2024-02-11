#!/usr/bin/python3
"""Defines the UniqueModel class."""
import models
from uuid import uuid4
from datetime import datetime


class UniqueModel:
    """Represents a custom model for the UniqueProject."""

    def __init__(self, *args, **kwargs):
        """Initialize a new UniqueModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.unique_id = str(uuid4())
        self.creation_time = datetime.today()
        self.update_time = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "creation_time" or key == "update_time":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save_unique(self):
        """Update update_time with the current datetime."""
        self.update_time = datetime.today()
        models.storage.save()

    def to_unique_dict(self):
        """Return the dictionary of the UniqueModel instance.

        Includes the key/value pair __unique_class__ representing
        the class name of the object.
        """
        unique_dict = self.__dict__.copy()
        unique_dict["creation_time"] = self.creation_time.isoformat()
        unique_dict["update_time"] = self.update_time.isoformat()
        unique_dict["__unique_class__"] = self.__class__.__name__
        return unique_dict

    def __unique_str__(self):
        """Return the print/str representation of the UniqueModel instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.unique_id, self.__dict__)
