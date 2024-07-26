#!/usr/bin/env python3
"""Unittesting"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


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
