#!/usr/bin/python3
"""Unittest module for the BaseModel Class.
"""

import unittest
from unittest import TestCase
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(TestCase):
    """A class for various test cases for the BaseModel
    """

    def setUp(self):
        self.b_model = BaseModel()
        self.b_model2 = BaseModel()

    def test_attr_id_instance(self):
        """Test the attr `id` for the correct instance
        """
        self.assertIsInstance(self.b_model.id, str)

    def test_attr_created_at_instance(self):
        """Test the instance attr `created_at`
        """
        self.assertIsInstance(self.b_model.created_at, datetime)

    def test_attr_updated_at_instance(self):
        """Test the instance attr `updated_at`
        """
        self.assertIsInstance(self.b_model.updated_at, datetime)

    def test_base_model_save_method(self):
        """Test the save method in base_model
        """
        self.b_model.save()
        self.assertIsInstance(self.b_model.updated_at, datetime)

    def test_base_model_to_dict_method(self):
        """Test to_dict method in base_model
        """
        self.b_model.to_dict()
        self.assertIsInstance(self.b_model.to_dict(), dict)

    def test_base_model_to_dict_correct_type(self):
        """Test for the correct type of to_dict method
        """
        content = self.b_model.to_dict()
        self.assertEqual(type(content['created_at']), str)
        self.assertEqual(type(content['updated_at']), str)
        self.assertEqual(type(content['id']), str)
        self.assertEqual(type(content['__class__']), str)

    def test_create_base_model_from_dict(self):
        """Test the create BaseModel from dictionary
        """
        content = self.b_model.to_dict()
        b_model2 = BaseModel(**content)
        self.assertEqual(b_model2.id, self.b_model.id)
        self.assertEqual(type(b_model2.created_at), datetime)
        self.assertEqual(type(b_model2.updated_at), datetime)
        self.assertEqual(b_model2.created_at, self.b_model.created_at)
        self.assertEqual(b_model2.updated_at, self.b_model.updated_at)

    def test_two_equal_object(self):
        """Teste if a new object created is same as first object
        """
        content = self.b_model.to_dict()
        b_model2 = BaseModel(**content)
        self.assertIsNot(self.b_model, b_model2)


if __name__ == "__main__":
    unittest.main()
