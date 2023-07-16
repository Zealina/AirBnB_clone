#!/usr/bin/python3
"""Module for ``test_city``
"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test suite for the class: City
    """

    def setUp(self):
        """Runs before before a test case runs
        """
        self.city = City()

    def test_city_attr_name(self):
        """Test case for name attribute"""
        self.assertIsInstance(self.city.name, str)

    def test_city_attr_state_id(self):
        """Test case for the state_id attribute"""
        self.assertIsInstance(self.city.state_id, str)


if __name__ == "__main__":
    unittest.main()
