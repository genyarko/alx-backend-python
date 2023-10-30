#!/usr/bin/env python3

import unittest
from parameterized import parameterized
from utils import access_nested_map  # Import your access_nested_map function

class TestAccessNestedMap(unittest.TestCase):
    """
    Unit tests for the access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),                  # Test case 1
        ({"a": {"b": 2}}, ("a",), {"b": 2}),    # Test case 2
        ({"a": {"b": 2}}, ("a", "b"), 2),      # Test case 3
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test the access_nested_map function for various inputs.
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
