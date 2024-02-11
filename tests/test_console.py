import unittest
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch
import os


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        del self.console

    def test_quit_command(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.assertTrue(self.console.onecmd("quit"))
            self.assertEqual(mock_stdout.getvalue().strip(), "")

    def test_help_command(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("help")
            self.assertIn("Documented commands (type help <topic>):", mock_stdout.getvalue())

    def test_create_command(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) == 36 and all(c.isalnum() for c in output))

    def test_show_command(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("show BaseModel 1234-5678")
            self.assertIn("** no instance found **", mock_stdout.getvalue())

    def test_destroy_command(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("destroy BaseModel 1234-5678")
            self.assertIn("** no instance found **", mock_stdout.getvalue())

    def test_all_command(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("all")
            self.assertIn("[]", mock_stdout.getvalue())

    def test_update_command(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.console.onecmd("update BaseModel 1234-5678 name 'John'")
            self.assertIn("** no instance found **", mock_stdout.getvalue())

    # Add more tests for other commands and features

if __name__ == '__main__':
    unittest.main()
