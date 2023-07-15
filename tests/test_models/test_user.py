#!/usr/bin/python3
"""Unittest module for the User Class.
"""
import unittest
from models.user import User
from unittest import TestCase


class TestUser(TestCase):
    """Test cases for the User class
    """

    def setUp(self):
        self.user = User()

    def test_class_attr_email(self):
        """Test the correct instance for the class attribute ``email``
        """
        self.assertIsInstance(self.user.email, str)

    def test_class_attr_password(self):
        """Test the correct instance for the class attribute ``password``
        """
        self.assertIsInstance(self.user.password, str)

    def test_class_attr_first_name(self):
        """Test the correct instance for the class attribute ``first_name``
        """
        self.assertIsInstance(self.user.first_name, str)

    def test_class_attr_last_name(self):
        """Test the correct instance for the class attribute``last_name``
        """
        self.assertIsInstance(self.user.last_name, str)


if __name__ == "__main__":
    unittest.main()
