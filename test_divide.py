#!/usr/bin/env python3
"""
Тесты для функции деления
"""

import unittest
from calculator import divide

class TestDivideFunction(unittest.TestCase):
    """Тесты функции divide()"""
    
    def test_divide_positive_numbers(self):
        """Деление положительных чисел"""
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(100, 10), 10)
        self.assertEqual(divide(9, 3), 3)
    
    def test_divide_negative_numbers(self):
        """Деление отрицательных чисел"""
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(10, -2), -5)
        self.assertEqual(divide(-12, -3), 4)
    
    def test_divide_decimals(self):
        """Деление десятичных чисел"""
        self.assertEqual(divide(5.0, 2.0), 2.5)
        self.assertEqual(divide(1.5, 0.5), 3.0)
        self.assertEqual(divide(0.6, 0.2), 3.0)
    
    def test_divide_by_one(self):
        """Деление на единицу"""
        self.assertEqual(divide(7, 1), 7)
        self.assertEqual(divide(0, 1), 0)
        self.assertEqual(divide(-5, 1), -5)
    
    def test_divide_zero_by_number(self):
        """Деление нуля на число"""
        self.assertEqual(divide(0, 5), 0)
        self.assertEqual(divide(0, -3), 0)

if __name__ == "__main__":
    unittest.main()
