#!/usr/bin/env python3
"""
Unit test for utils functions
"""
from unittest import TestCase
from parameterized import parameterized

access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(TestCase):
    """
    A test class for access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """A test method for access_nested_map function
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test method to check whether exception is raised
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
