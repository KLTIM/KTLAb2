#!/usr/bin/env python3
"""
Тесты для функции вычитания
"""

import unittest
from calculator import subtract

class TestSubtractFunction(unittest.TestCase):
    """Тесты функции subtract()"""
    
    def test_subtract_positive_numbers(self):
        """Вычитание положительных чисел"""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(100, 75), 25)
    
    def test_subtract_negative_numbers(self):
        """Вычитание отрицательных чисел"""
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(-5, 2), -7)
        self.assertEqual(subtract(3, -4), 7)
    
    def test_subtract_zero(self):
        """Вычитание с нулем"""
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(5, 0), 5)
        self.assertEqual(subtract(0, 3), -3)
    
    def test_subtract_decimals(self):
        """Вычитание десятичных чисел"""
        self.assertEqual(subtract(5.5, 2.5), 3.0)
        self.assertEqual(subtract(3.3, 1.1), 2.2)
        self.assertEqual(subtract(0.5, 0.2), 0.3)
    
    def test_subtract_result_negative(self):
        """Вычитание с отрицательным результатом"""
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(1, 10), -9)

if __name__ == "__main__":
    unittest.main()
