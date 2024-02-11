#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represents an abstracted storage engine.

    Attributes:
        __file_path (str): The file name for saving objects.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets obj with key <obj_class_name>.id in __objects."""
        obj_class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_class_name, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file __file_path."""
        objects_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(objects_dict, file)

    def reload(self):
        """Deserializes a JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as file:
                objects_dict = json.load(file)
                for obj_data in objects_dict.values():
                    class_name = obj_data.pop("__class__")
                    self.new(eval(class_name)(**obj_data))
        except FileNotFoundError:
            return
