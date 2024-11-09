#!/usr/bin/env python3
""" Defines test class for utils.access_nested_map function """

from parameterized import parameterized
from typing import Dict, Tuple, Union
import unittest
import utils
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """ Provides functionality for testing utils.access_nested_map """

    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self,
                               nested_map: Dict,
                               path: Tuple[str],
                               expected: Union[Dict, int]
                               ) -> None:
        """ Performs unit tests on utils.access_nested_map """
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a"), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
        ])
    def test_access_nested_map_exception(self,
                                         nested_map: Dict,
                                         path: Tuple[str],
                                         exception: Exception
                                         ) -> None:
        """ Tests that utils.access_nested_map returns expected o/p """
        with self.assertRaises(exception):
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Tests that utils.get_json returns expected result """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(self,
                      test_url: str,
                      test_payload: Dict
                      ) -> Dict:
        """ Tests that utils.get_json returns expected output """
        mocked_attrs = {"json.return_value": test_payload}
        with patch("requests.get", return_value=Mock(**mocked_attrs)) as res:
            self.assertEqual(utils.get_json(test_url), test_payload)
            res.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ Provides functionality to test utils.memoize """

    def test_memoize(self) -> None:
        """ Tests utils.memoize """

        class TestClass:
            def a_method(self):
                return 42

            @utils.memoize
            def a_property(self):
                return self.a_method()

        with patch.object(
                          TestClass,
                          "a_method",
                          return_value=lambda: 42
                          ) as memoized_fn:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memoized_fn.assert_called_once()
