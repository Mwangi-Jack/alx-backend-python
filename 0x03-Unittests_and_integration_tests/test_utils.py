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
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False})
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


class TestMemoize(unittest.TestCase):
    """This class defines methods to test the memoize decorator"""

    def test_memoize(self):
        """This method tests the memoize decorator"""
        class TestClass:
            """Test class"""
            def a_method(self):
                """This method returns an integer value 42"""
                return 42

            @memoize
            def a_property(self):
                """This method returns the out put of a_method func"""
                return self.a_method

        with patch.object(TestClass, 'a_method',
                          return_value=24) as mock_a_method:
            thing = TestClass()
            thing.a_method()

        result1 = thing.a_property()
        result2 = thing.a_property()
        self.assertEqual(result1, result2)
        mock_a_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
