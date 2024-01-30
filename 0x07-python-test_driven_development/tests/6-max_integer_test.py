#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([]), None)

    def test_with_neg(self):
        self.assertEqual(max_integer([-1, 2, 3, 4, -8, 7]), 7)
        self.assertEqual(max_integer([-1, -2, -3, -4, -5, -7]), -1)

    def test_with_pos(self):
        self.assertEqual(max_integer([10, 5, 8]), 10)
        self.assertEqual(max_integer([8, 10, 5]), 10)
        self.assertEqual(max_integer([5, 8, 10]), 10)
