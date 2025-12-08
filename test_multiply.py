#!/usr/bin/env python3
"""
Тесты для функции умножения
"""

import unittest
from calculator import multiply

class TestMultiplyFunction(unittest.TestCase):
    """Тесты функции multiply()"""
    
    def test_multiply_positive_numbers(self):
        """Умножение положительных чисел"""
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(5, 6), 30)
        self.assertEqual(multiply(7, 8), 56)
    
    def test_multiply_negative_numbers(self):
        """Умножение отрицательных чисел"""
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(4, -5), -20)
        self.assertEqual(multiply(-3, -4), 12)
    
    def test_multiply_by_zero(self):
        """Умножение на ноль"""
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(10, 0), 0)
        self.assertEqual(multiply(0, 0), 0)
    
    def test_multiply_decimals(self):
        """Умножение десятичных чисел"""
        self.assertEqual(multiply(2.5, 4), 10.0)
        self.assertEqual(multiply(1.5, 2.0), 3.0)
        self.assertEqual(multiply(0.5, 0.5), 0.25)
    
    def test_multiply_by_one(self):
        """Умножение на единицу"""
        self.assertEqual(multiply(1, 7), 7)
        self.assertEqual(multiply(9, 1), 9)
        self.assertEqual(multiply(1, 1), 1)

if __name__ == "__main__":
    unittest.main()
