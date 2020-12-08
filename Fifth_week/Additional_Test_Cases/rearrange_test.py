#! /usr/bin/env python3

from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testCase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testCase), expected)

    #Edge cases are inputs to our code that produce unexpected results, and are found at the
    #extreme ends of the ranges of input we image our programs will typically work with
    
    def test_empty(self):
        testCase = ""
        expected = ""
        self.assertEqual(rearrange_name(testCase), expected)

    def test_double_name(self):
        testCase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testCase), expected)

    def test_one_name(self):
        testCase = "Axel"
        expected = "Axel"
        self.assertEqual(rearrange_name(testCase), expected)

unittest.main()