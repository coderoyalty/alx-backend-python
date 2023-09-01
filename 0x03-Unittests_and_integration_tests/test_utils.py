#!/usr/bin/env python3
"""
unittest for utils.py
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Test class for `utils.access_nested_map`
    """
    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ],)
    def test_access_nested_map(self, nested_map, path, expected):
        """test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
