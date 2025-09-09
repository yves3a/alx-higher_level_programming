#!/usr/bin/python3
"""Unit tests for greeting module."""

import unittest
from greeting import greeting_response


class TestGreeting(unittest.TestCase):
    """Test cases for greeting functionality."""
    
    def test_greeting_response_returns_hi(self):
        """Test that greeting_response returns 'hi'."""
        result = greeting_response()
        self.assertEqual(result, "hi")
    
    def test_greeting_response_type(self):
        """Test that greeting_response returns a string."""
        result = greeting_response()
        self.assertIsInstance(result, str)


if __name__ == "__main__":
    unittest.main()