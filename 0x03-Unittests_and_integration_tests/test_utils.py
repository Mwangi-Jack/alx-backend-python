#!/usr/bin/env python3
"""Unittests and Intergration Tests"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json


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
    @patch('requests.get')
    def test_get_json(self, url, payload, mock_get):
        """Test for getting JSON"""

        mock_response = Mock()
        mock_response.json.return_value = payload
        mock_get.return_value = mock_response
        result = get_json(url)

        self.assertIsNotNone(result)
        self.assertEqual(result, payload)
        mock_get.assert_called_once_with(url)
