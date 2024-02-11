#!/usr/bin/python3
"""Defines the HBNB console."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def extract_enclosed_text(arg, pattern):
    result = re.search(pattern, arg)
    if result is None:
        return [i.strip(",") for i in split(arg)]
    else:
        lexer = split(arg[:result.span()[0]])
        return [i.strip(",") for i in lexer] + [result.group()]


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    valid_classes =
    {"BaseModel", "User", "State", "City", "Place", "Amenity", "Review"}

    def emptyline(self):
        """Do not something upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default action for the cmd module when an invalid cmd is entered.
        """
        arg_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            arg_list = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg_list[1])
            if match is not None:
                command = [arg_list[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in arg_dict.keys():
                    call = "{} {}".format(arg_list[0], command[1])
                    return arg_dict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """Usage: create <class>
        Create a brand new magnificence instance and print its identification
        """
        arg_list = extract_enclosed_text(arg, r"\{(.*?)\}|\[(.*?)\]")
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg_list[0])().id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Show the string illustration of a class example of a given identity.
        """
        arg_list = extract_enclosed_text(arg, r"\{(.*?)\}|\[(.*?)\]")
        obj_dict = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.valid_classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(arg_list[0], arg_list[1])])

    # Rest of the code remains unchanged...
