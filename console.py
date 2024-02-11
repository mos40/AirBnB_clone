#!/usr/bin/python3
"""
Command interpreter module.
"""

import cmd


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
