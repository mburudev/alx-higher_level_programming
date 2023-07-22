#!/usr/bin/python3
"""Unittests for max_integer([..])."""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_negative_integers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_mixed_integers(self):
        self.assertEqual(max_integer([-5, 2, -9, 10, 0]), 10)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.7, 3.9, 4.1]), 4.1)

    def test_single_element_list(self):
        self.assertEqual(max_integer([7]), 7)

    def test_duplicate_elements(self):
        self.assertEqual(max_integer([10, 10, 10]), 10)

    def test_mixed_elements(self):
        self.assertEqual(max_integer([1, "hello", 3]), 3)

    def test_nested_lists(self):
        self.assertEqual(max_integer([[1, 2], [3, 4], [5, 6]]), [5, 6])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_integer("invalid")


if __name__ == '__main__':
    unittest.main()
