#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_void(self):
        """if no argument"""
        self.assertIsNone(max_integer())
        self.assertIsNone(max_integer([]))

    def test_max(self):
        """if valid argument, return max integer of the list"""
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([-1, 2, 3]), 3)

    def test_raises(self):
        """If the argument is not a list"""
        self.assertRaises(TypeError, max_integer, 10)
        self.assertRaises(TypeError, max_integer, 10.0)


"""python3 -m unittest tests.6-max_integer_test 2>&1 | tail -1"""
