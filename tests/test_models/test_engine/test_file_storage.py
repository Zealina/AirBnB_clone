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
        """Sets up test methods."""
        pass

    def resetStorage(self):
        """Resets the data in FileStorage"""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def tearDown(self):
        """Tears down the methods"""
        self.resetStorage()
        pass

    def test_raise_private_attr_err(self):
        """Test for attribute error if private attributesis being accessed"""
        f_storage = FileStorage()
        with self.assertRaises(AttributeError):
            f_storage.__file_path
        with self.assertRaises(AttributeError):
            f_storage.__object

    def test_methods_all(self):
        """Test a method named all for right return type
        """
        f_storage = FileStorage()
        self.assertEqual(type(f_storage.all()), dict)

    def test_method_new(self):
        """Test a method named new
        """
        b_model = BaseModel()
        f_storage = FileStorage()
        f_storage.new(b_model)
        f_storage_keys = f_storage.all().keys()
        self.assertIn(
            f'{b_model.__class__.__name__}.{b_model.id}', f_storage_keys)

    def test_method_save(self):
        """Test a method named save
        """
        f_storage = FileStorage()
        f_storage.save()

    def test_method_reload(self):
        """Test a method named reload
        """
        f_storage = FileStorage()
        f_storage.reload()


if __name__ == '__main__':
    unittest.main()
