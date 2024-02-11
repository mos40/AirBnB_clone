import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def capture_stdout(self, command):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.console.onecmd(command)
            return mock_stdout.getvalue()

    def test_create(self):
        output = self.capture_stdout("create BaseModel")
        self.assertTrue(len(output) == 36 and isinstance(output, str))

    def test_create_missing_class(self):
        output = self.capture_stdout("create")
        self.assertEqual(output.strip(), "** class name missing **")

    def test_create_invalid_class(self):
        output = self.capture_stdout("create InvalidClass")
        self.assertEqual(output.strip(), "** class doesn't exist **")

    def test_show(self):
        output = self.capture_stdout("show BaseModel 1234-1234-1234")
        self.assertEqual(output.strip(), "** no instance found **")

    def test_show_missing_class(self):
        output = self.capture_stdout("show")
        self.assertEqual(output.strip(), "** class name missing **")

    def test_show_invalid_class(self):
        output = self.capture_stdout("show InvalidClass")
        self.assertEqual(output.strip(), "** class doesn't exist **")

    def test_show_missing_id(self):
        output = self.capture_stdout("show BaseModel")
        self.assertEqual(output.strip(), "** instance id missing **")

    def test_destroy(self):
        output = self.capture_stdout("destroy BaseModel 1234-1234-1234")
        self.assertEqual(output.strip(), "** no instance found **")

    def test_destroy_missing_class(self):
        output = self.capture_stdout("destroy")
        self.assertEqual(output.strip(), "** class name missing **")

    def test_destroy_invalid_class(self):
        output = self.capture_stdout("destroy InvalidClass")
        self.assertEqual(output.strip(), "** class doesn't exist **")

    def test_destroy_missing_id(self):
        output = self.capture_stdout("destroy BaseModel")
        self.assertEqual(output.strip(), "** instance id missing **")

    def test_all(self):
        output = self.capture_stdout("all BaseModel")
        self.assertTrue(output.startswith("[") and output.endswith("]"))

    def test_all_missing_class(self):
        output = self.capture_stdout("all")
        self.assertEqual(output.strip(), "** class doesn't exist **")

    def test_update(self):
        output = self.capture_stdout("update BaseModel 1234-1234-1234 name 'John'")
        self.assertEqual(output.strip(), "")

    def test_update_missing_class(self):
        output = self.capture_stdout("update")
        self.assertEqual(output.strip(), "** class name missing **")

    def test_update_invalid_class(self):
        output = self.capture_stdout("update InvalidClass")
        self.assertEqual(output.strip(), "** class doesn't exist **")

    def test_update_missing_id(self):
        output = self.capture_stdout("update BaseModel")
        self.assertEqual(output.strip(), "** instance id missing **")

    def test_update_invalid_id(self):
        output = self.capture_stdout("update BaseModel InvalidID")
        self.assertEqual(output.strip(), "** no instance found **")

    def test_update_missing_attribute(self):
        output = self.capture_stdout("update BaseModel 1234-1234-1234")
        self.assertEqual(output.strip(), "** attribute name missing **")

    def test_update_missing_value(self):
        output = self.capture_stdout("update BaseModel 1234-1234-1234 name")
        self.assertEqual(output.strip(), "** value missing **")


if __name__ == '__main__':
    unittest.main()
