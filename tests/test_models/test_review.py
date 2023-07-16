#!/usr/bin/python3
"""Module for the ``test_review``"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Class for the review test cases
    """

    def setUp(self):
        """Runs before a test case runs
        """
        self.review = Review()

    def test_review_attr_user_id(self):
        """Test case for the review attribute id
        """
        self.assertIsInstance(self.review.user_id, str)

    def test_review_attr_place_id(self):
        """Test case for the review attribute place_id"""
        self.assertIsInstance(self.review.place_id, str)

    def test_review_attr_text(self):
        self.assertIsInstance(self.review.text, str)


if __name__ == "__main__":
    unittest.main()
