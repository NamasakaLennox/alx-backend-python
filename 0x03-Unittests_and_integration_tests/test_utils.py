#!/usr/bin/env python3
"""
Unit test for utils functions
"""
import unittest
from unittest import mock
from parameterized import parameterized

utils = __import__('utils')


class TestAccessNestedMap(unittest.TestCase):
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
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test method to check whether exception is raised
        """
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """A Test class for the get_json method
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @mock.patch('utils.requests')
    def test_get_json(self, url, payload, mock_requests):
        """A method implemented to test the get_json function
        """
        mock_response = mock.Mock()
        mock_response.json.return_value = payload

        mock_requests.get.return_value = mock_response

        self.assertEqual(utils.get_json(url), payload)
        mock_requests.get.assert_called_once()


class TestMemoize(unittest.TestCase):
    """A test calss for the memoize decorator function
    """
    def test_mock(self):
        """A test method for the memoize function
        """
        class TestClass:
            """Test class for memoize function
            """
            def a_method(self):
                """test method
                """
                return 42

            @utils.memoize
            def a_property(self):
                """Call the function to see how many times it's called
                """
                return self.a_method()

        with mock.patch.object(TestClass, 'a_method', return_value=42) as temp:
            test = TestClass()
            self.assertEqual(test.a_property, 42)
            self.assertEqual(test.a_property, 42)

        temp.assert_called_once_with()
