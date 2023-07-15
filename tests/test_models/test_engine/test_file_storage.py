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
        self.f_storage = FileStorage()
        self.b_model = BaseModel()

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

        with self.assertRaises(AttributeError):
            self.f_storage.__file_path
        with self.assertRaises(AttributeError):
            self.f_storage.__object

    def test_methods_all(self):
        """Test a method named all for right return type
        """
        self.assertEqual(type(self.f_storage.all()), dict)

    def test_method_new(self):
        """Test a method named new
        """
        self.f_storage.new(self.b_model)
        f_storage_keys = self.f_storage.all().keys()
        self.assertIn(
            f'{self.b_model.__class__.__name__}.{self.b_model.id}', f_storage_keys)

    def test_method_save(self):
        """Test a method named save
        """
        self.f_storage.save()

    def test_method_reload(self):
        """Test a method named reload
        """
        self.f_storage.reload()


if __name__ == '__main__':
    unittest.main()
