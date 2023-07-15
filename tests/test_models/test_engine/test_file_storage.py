#!/usr/bin/python3

"""This test module`(test_file_storage)` contains the
     test classes for the file_storage module
"""

from models.base_model import BaseModel
import unittest
from unittest import TestCase
from models.engine.file_storage import FileStorage


class TestFileStorage(TestCase):
    """A class that contains test cases for the FileStorage class"""

    def test_raise_private_attr_err(self):
        """Test for attribute error if private attributesis being accessed"""
        file_storage = FileStorage()
        with self.assertRaises(AttributeError):
            file_storage.__file_path
        with self.assertRaises(AttributeError):
            file_storage.__object

    def test_all(self):
        """Test all method for correct type"""
        pass


if __name__ == '__main__':
    unittest.main()
