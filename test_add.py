#!/usr/bin/env python3
"""
Тесты для функции сложения
"""

import unittest
from calculator import add

class TestAddFunction(unittest.TestCase):
    """Тесты функции add()"""
    
    def test_add_positive_numbers(self):
        """Сложение положительных чисел"""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(10, 20), 30)
        self.assertEqual(add(100, 200), 300)
    
    def test_add_negative_numbers(self):
        """Сложение отрицательных чисел"""
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(-5, 10), 5)
        self.assertEqual(add(3, -7), -4)
    
    def test_add_zero(self):
        """Сложение с нулем"""
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(5, 0), 5)
        self.assertEqual(add(0, 8), 8)
    
    def test_add_decimals(self):
        """Сложение десятичных чисел"""
        self.assertEqual(add(2.5, 3.5), 6.0)
        self.assertEqual(add(1.1, 2.2), 3.3)
        self.assertEqual(add(0.1, 0.2), 0.3)
    
    def test_add_large_numbers(self):
        """Сложение больших чисел"""
        self.assertEqual(add(1000000, 2000000), 3000000)
        self.assertEqual(add(999999, 1), 1000000)

if __name__ == "__main__":
    unittest.main()
