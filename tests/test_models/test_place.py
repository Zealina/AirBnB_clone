#!/usr/bin/python3
"""Module for the ``test_place``
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """A class for the various test cases for the place model
    """

    def setUp(self):
        """Runs before any test case runs"""
        self.place = Place()

    def test_place_attr_city_id(self):
        """Test case for the city attribute"""
        self.assertIsInstance(self.place.city_id, str)

    def test_place_attr_user_id(self):
        """Test case for the user_id attribute"""
        self.assertIsInstance(self.place.user_id, str)

    def test_place_attr_name(self):
        """Test case for the name attribute"""
        self.assertIsInstance(self.place.name, str)

    def test_place_attr_description(self):
        """Test case for the description attribute"""
        self.assertIsInstance(self.place.description, str)

    def test_place_attr_number_rooms(self):
        """Test case for the number_rooms attribute"""
        self.assertIsInstance(self.place.number_rooms, int)

    def test_place_attr_number_bathrooms(self):
        """Test case for the number_bathrooms attribute"""
        self.assertIsInstance(self.place.number_bathrooms, int)

    def test_place_attr_max_guest(self):
        """Test case for the max_guest attribute"""
        self.assertIsInstance(self.place.max_guest, int)

    def test_place_attr_price_by_night(self):
        """Test case for the price_by_night attribute"""
        self.assertIsInstance(self.place.price_by_night, int)

    def test_place_attr_latitude(self):
        """Test case for the lattiude attribute"""
        self.assertIsInstance(self.place.latitude, float)

    def test_place_attr_longitude(self):
        """Test case for the longitude attribute"""
        self.assertIsInstance(self.place.longitude, float)

    def test_place_attr_amenity_ids(self):
        """Test case for the amenity_ids attribute"""
        self.assertIsInstance(self.place.amenity_ids, list)
