#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""

import cmd
import json
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class.

    Attributes:
        prompt (str): The prompt string for the command interpreter.
    """

    prompt = "(hbnb) "
    valid_classes = ["BaseModel"]

    def do_quit(self, arg):
        """
        Quit command to exit the program.

        Args:
            arg (str): The argument passed to the command. Ignored.

        Returns:
            bool: True to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program at end-of-file.

        Args:
            arg (str): The argument passed to the command. Ignored.

        Returns:
            bool: True to exit the program.
        """
        print("")
        return True

    def emptyline(self):
        """
        Do nothing on an empty line.
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file), and prints the id.

        Args:
            arg (str): The class name.

        Example:
            $ create BaseModel
        """
        if not arg:
            print("** class name missing **")
        elif arg not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id.

        Args:
            arg (str): The class name and instance id.

        Example:
            $ show BaseModel 1234-1234-1234
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            obj_dict = models.storage.all()
            if key not in obj_dict:
                print("** no instance found **")
            else:
                print(obj_dict[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and
        id (saves the change into the JSON file).

        Args:
            arg (str): The class name and instance id.

        Example:
            $ destroy BaseModel 1234-1234-1234
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            obj_dict = models.storage.all()
            if key not in obj_dict:
                print("** no instance found **")
            else:
                del obj_dict[key]
                models.storage.save()

    def do_all(self, arg):
        """
        Prints all string representations of all
        instances based or not on the class name.

        Args:
            arg (str): The class name.

        Example:
            $ all BaseModel
        """
        obj_dict = models.storage.all()
        result = []
        if not arg:
            for obj in obj_dict.values():
                result.append(str(obj))
        elif arg not in self.valid_classes:
            print("** class doesn't exist **")
            return
        else:
            for key, obj in obj_dict.items():
                if key.split('.')[0] == arg:
                    result.append(str(obj))
        print(result)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and
        id by adding or updating attribute.

        Args:
            arg (str): The class name, instance id, attribute name,
            and attribute value.

        Example:
            $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            obj_dict = models.storage.all()
            if key not in obj_dict:
                print("** no instance found **")
            else:
                obj = obj_dict[key]
                attr_name = args[2]
                attr_value = args[3]
                setattr(obj, attr_name, attr_value)
                obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
