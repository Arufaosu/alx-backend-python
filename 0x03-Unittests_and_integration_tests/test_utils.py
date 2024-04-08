#!/usr/bin/env python3
"""test_utils.py"""
import unittest
from parameterized import parameterized
from utils import *
from unittest.mock import patch

class TestAccessNestedMap(unittest.TestCase):
    "test access nested map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test utils.access_nested_map results"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'")
    ])
    def test_access_nested_map_exception(self, nested_map, path, error_msg):
        """test utils.access_nested_map KeyError exception"""
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(str(error.exception), error_msg)


class TestGetJson(unittest.TestCase):
    """tests for utils.get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, url, expected_response, mock_get):
        """test utils.get_json returned response"""

        mock_get.return_value.json.return_value = expected_response

        result = get_json(url)

        mock_get.assert_called_once_with(url)

        self.assertEqual(result, expected_response)


class TestMemoize(unittest.TestCase):
    """tests for utils.memoize function"""

    def test_memoize(self):
        """test utils.memoize function"""

        class TestClass:
            """helper class"""

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_instance = TestClass()

        with patch.object(TestClass, 'a_method') as mock_method:
            mock_method.return_value = 42

            test_instance.a_property
            res = test_instance.a_property

            mock_method.assert_called_once()

            self.assertEqual(res, 42)
