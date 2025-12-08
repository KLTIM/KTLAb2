#!/usr/bin/env python3
"""
Тесты для обработки ошибок и edge cases
"""

import unittest
from calculator import divide, add, subtract, multiply

class TestErrorCases(unittest.TestCase):
    """Тесты обработки ошибок и граничных случаев"""
    
    def test_divide_by_zero_raises_error(self):
        """Деление на ноль вызывает исключение"""
        with self.assertRaises(ValueError):
            divide(10, 0)
        
        with self.assertRaises(ValueError):
            divide(0, 0)
        
        with self.assertRaises(ValueError):
            divide(-5, 0)
    
    def test_divide_by_zero_error_message(self):
        """Проверка сообщения об ошибке при делении на ноль"""
        with self.assertRaises(ValueError) as context:
            divide(10, 0)
        
        self.assertEqual(str(context.exception), "Cannot divide by zero")
    
    def test_large_numbers_operations(self):
        """Операции с очень большими числами"""
        self.assertEqual(add(1000000000, 2000000000), 3000000000)
        self.assertEqual(subtract(3000000000, 1000000000), 2000000000)
        self.assertEqual(multiply(1000000, 2000), 2000000000)
    
    def test_floating_point_precision(self):
        """Тест точности вычислений с плавающей точкой"""
        # Используем almostEqual для сравнения с плавающей точкой
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=7)
        self.assertAlmostEqual(subtract(0.3, 0.1), 0.2, places=7)
        self.assertAlmostEqual(multiply(0.1, 0.2), 0.02, places=7)
        self.assertAlmostEqual(divide(0.1, 0.2), 0.5, places=7)
    
    def test_operation_chaining(self):
        """Тест последовательных операций"""
        result = add(5, 3)
        result = multiply(result, 2)
        result = subtract(result, 4)
        result = divide(result, 2)
        
        self.assertEqual(result, 6.0)

if __name__ == "__main__":
    unittest.main()
