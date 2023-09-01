#!/usr/bin/env python3
"""
unittest for utils.py
"""
import unittest
import unittest.mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
import requests


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

    @parameterized.expand([
        ({}, ("a")),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """test access_nested_map for exception"""
        with self.assertRaises(KeyError) as err:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    unittest class for utils.get_json
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ test utils.get_json """

        with unittest.mock.patch('requests.get') as mock:
            mock.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)

            # assert the mock was called once with the URL
            mock.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    unittest for `utils.memoize`
    """

    def test_memoize(self):
        """test utils.memoize"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with unittest.mock.patch.object(TestClass, 'a_method') as mock:
            obj = TestClass()
            obj.a_property()
            obj.a_property()
            mock.assert_called_once()
