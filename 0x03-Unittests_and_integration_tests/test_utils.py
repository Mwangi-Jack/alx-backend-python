#!/usr/bin/env python3
"""Unittests and Intergration Tests"""

import unittest
from unittest.mock import patch, MagicMock

from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    This class holds the methods to test the
    access_nested_map method
    """
    @parameterized.expand([({"a": 1}, ('a',), 1),
                           ({"a": {"b": 2}}, ("a",), {'b': 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2)
                           ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test case"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ('a',)), ({'a': 1}, ('a', 'b'))])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test for key error"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """This class hold methods to test for HTTP calls"""

    @parameterized.expand([
        ('https://example.com', {'payload': True}),
        ('https://holberton.io', {'payload': False})
    ])
    @patch('utils.requests')
    def test_get_json(self, set_url, expected_payload, mock_get):
        """Test for getting JSON"""

        mock_response = MagicMock(return_value=200)
        mock_response.json.return_value = expected_payload
        mock_get.get.return_value = mock_response
        result = get_json(set_url)

        self.assertIsNotNone(result)
        self.assertEqual(result, expected_payload)
        mock_get.get.assert_called_once_with(set_url)

# class TestMemoize(unittest.TestCase):
#     """This class defines methods to test the memoize decorator"""

#     def test_memoize(self):
#         """This method tests the memoize decorator"""
#         class TestClass:
#             def a_method(self):
#                 return 42

#             @memoize
#             def a_property(self):
#                 return self.a_method




if __name__ == '__main__':
    unittest.main()
