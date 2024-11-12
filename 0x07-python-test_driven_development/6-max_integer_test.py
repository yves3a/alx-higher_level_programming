#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class to test the max_integer function"""

    def test_ordered_list(self):
        """Test an ordered list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_negative_numbers(self):
        """Test a list with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test a list with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-2, -1, 0, -3, -4]), 0)

    def test_floats(self):
        """Test a list of floating point numbers"""
        self.assertEqual(max_integer([2.4, 3.5, 1.2]), 3.5)

    def test_single_element(self):
        """Test a list with a single element"""
        self.assertEqual(max_integer([5]), 5)

    def test_identical_elements(self):
        """Test a list with identical elements"""
        self.assertEqual(max_integer([7, 7, 7]), 7)

    def test_string_list(self):
        """Test a list of strings"""
        self.assertEqual(max_integer(['a', 'b', 'c']), 'c')

    def test_mixed_types(self):
        """Test that the function raises TypeError for mixed types"""
        with self.assertRaises(TypeError):
            max_integer([1, 'b', 3])


if __name__ == '__main__':
    unittest.main()
