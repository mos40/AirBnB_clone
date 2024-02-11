#!/usr/bin/python3
"""
Command interpreter module.
"""

import cmd
import json
import models
from models import storage
from models.base_model import BaseModel
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class.
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """
        Do nothing on empty input line.
        """
        pass

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Handle EOF (Ctrl+D) to exit the program.
        """
        print()
        return True

    def help_quit(self):
        """
        Display help for quit command.
        """
        print("Quit command to exit the program")

    def help_EOF(self):
        """
        Display help for EOF (Ctrl+D) command.
        """
        print("Handle EOF (Ctrl+D) to exit the program")

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it to the JSON file, and prints the id.
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                cls = eval(args[0])
            except NameError:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (saves the change into the JSON file).
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                cls = eval(args[0])
            except NameError:
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representations of all instances based or not on the class name.
        """
        args = arg.split()
        objects = storage.all()
        if not args:
            print([str(obj) for obj in objects.values()])
        else:
            try:
                cls = eval(args[0])
                print([str(obj) for key, obj in objects.items() if args[0] in key])
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute
        (saves the change into the JSON file).
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls = eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                obj = storage.all()[key]
                setattr(obj, args[2], args[3][1:-1] if '"' in args[3] else args[3])
                obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
