#!/usr/bin/python3
"""Defines unittests for console.py.

Unittest classes:
    TestHBNBCommand_prompting
    TestHBNBCommand_help
    TestHBNBCommand_exit
    TestHBNBCommand_create
    TestHBNBCommand_show
    TestHBNBCommand_all
    TestHBNBCommand_destroy
    TestHBNBCommand_update
"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage


class TestConsole(unittest.TestCase):

    def test_help_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            output = f.getvalue().strip()
            self.assertTrue("Documented commands" in output)

    def test_create_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(output.startswith("b"))

    def test_show_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd(f"show BaseModel {obj}")
            output = f.getvalue().strip()
            self.assertTrue("BaseModel" in output)

    def test_all_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("all BaseModel")
            output = f.getvalue().strip()
            self.assertTrue("BaseModel" in output)

    def test_update_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            obj = HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd(f"update BaseModel {obj} name 'New Name'")
            updated_obj = storage.all()["BaseModel.{}".format(obj)]
            self.assertEqual(updated_obj.name, 'New Name')

    def test_quit_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            with self.assertRaises(SystemExit):
                HBNBCommand().onecmd("quit")

    # Add more test cases as needed for other commands and features

    unittest.main()
