#!/usr/bin/python3

"""This test module`(test_file_storage)` contains the
     test classes for the file_storage module
"""

from models.base_model import BaseModel
import unittest
from unittest import TestCase
from models.engine.file_storage import FileStorage
from models import storage
import os


class TestFileStorage(TestCase):
    """A class that contains test cases for the FileStorage class"""

    def setUp(self):
        """set up the test environment before each test is run"""
        dict_key = []
        for key in storage._FileStorage__objects.keys():
            dict_key.append(key)
        for key in dict_key:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """Clears storage file after tests end"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_raise_private_attr_err(self):
        """Test for attribute error if private attributesis being accessed"""
        file_storage = FileStorage()
        with self.assertRaises(AttributeError):
            file_storage.__file_path
        with self.assertRaises(AttributeError):
            file_storage.__object

    def test_methods_all(self):
        """Test a method named all for right return type
        """
        fs = FileStorage()
        self.assertEqual(type(fs.all()), dict)

    def test_method_new(self):
        """Test a method named new 
        """
        b = BaseModel()
        fs = FileStorage()
        fs.new(b)
        fs_keys = fs.all().keys()
        self.assertIn(f'{b.__class__.__name__}.{b.id}', fs_keys)

    def test_method_save(self):
        """Test a method named save
        """
        fs = FileStorage()
        fs.save()

    def test_method_reload(self):
        """Test a method named reload
        """
        fs = FileStorage()
        fs.reload()


if __name__ == '__main__':
    unittest.main()
