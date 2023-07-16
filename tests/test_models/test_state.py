#!/usr/bin/python3
"""Module for ``test_state``
"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test suit for the class: State"""

    def setUp(self):
        """Runs before a test case runs
        """
        self.state = State()

    def test_state_attr_name(self):
        self.assertIsInstance(self.state.name, str)


if __name__ == "__main__":
    unittest.main()
