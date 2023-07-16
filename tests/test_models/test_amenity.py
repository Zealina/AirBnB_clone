#!/usr/bin/python3
"""Module for ``test_amenity``"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test suite for Amenity class
    """

    def setUp(self):
        self.amenity = Amenity()

    def test_amentiy_attr_name(self):
        """Test cae for the name attribute"""
        self.assertIsInstance(self.amenity.name, str)


if __name__ == "__main__":
    unittest.main()
