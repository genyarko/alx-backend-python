#!/usr/bin/env python3
"""A module for testing the utils module.
"""

import unittest
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock
from parameterized import parameterized

from utils import (
    access_nested_map,
    get_json,
    memoize,
)

class TestAccessNestedMap(unittest.TestCase):
    """Test cases for the `access_nested_map` function."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),                  # Test case 1: Accessing a simple key
        ({"a": {"b": 2}}, ("a",), {"b": 2}),    # Test case 2: Accessing a nested key
        ({"a": {"b": 2}}, ("a", "b"), 2),      # Test case 3: Accessing a deeply nested key
    ])
    def test_access_nested_map(self, nested_map: Dict, path: Tuple[str], expected: Union[Dict, int]) -> None:
        """Test the `access_nested_map` function's output."""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),                 # Test case 4: Key not found in an empty dictionary
        ({"a": 1}, ("a", "b"), KeyError),      # Test case 5: Nested key not found
    ])
    def test_access_nested_map_exception(self, nested_map: Dict, path: Tuple[str], exception: Exception) -> None:
        """Test that `access_nested_map` raises the expected exception."""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    """Test cases for the `get_json` function."""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),    # Test case 6: Successful JSON retrieval
        ("http://holberton.io", {"payload": False}),  # Test case 7: Successful JSON retrieval
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """Test the `get_json` function's output."""
        attrs = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            result = get_json(test_url)
            self.assertEqual(result, test_payload)
            req_get.assert_called_once_with(test_url)

class TestMemoize(unittest.TestCase):
    """Test cases for the `memoize` function."""
    def test_memoize(self) -> None:
        """Test that `memoize` caches function results."""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, "a_method", return_value=42) as memo_fxn:
            test_class = TestClass()
            result1 = test_class.a_property()
            result2 = test_class.a_property()
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            memo_fxn.assert_called_once()

if __name__ == "__main__":
    unittest.main()
