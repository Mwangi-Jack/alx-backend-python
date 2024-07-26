#!/usr/bin/env python3

from parameterized import parameterized, parameterized_class
import unittest

@parameterized([
	(2, 2),
	(2, 1),
	(4, 4)
])
def test_equality(exponent, expected):
    """Test equality"""
    assert exponent, expected
