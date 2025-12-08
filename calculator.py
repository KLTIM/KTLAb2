#!/usr/bin/env python3

def add(a: float, b: float) -> float:
    """Сложение двух чисел с округлением"""
    return round(a + b, 10)  # Округляем до 10 знаков

def subtract(a: float, b: float) -> float:
    """Вычитание двух чисел с округлением"""
    return round(a - b, 10)

def multiply(a: float, b: float) -> float:
    """Умножение двух чисел с округлением"""
    return round(a * b, 10)

def divide(a: float, b: float) -> float:
    """Деление двух чисел"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return round(a / b, 10)

def main():
    """Точка входа для запуска как скрипт"""
    print("Calculator operations:")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"4 * 6 = {multiply(4, 6)}")
    print(f"10 / 2 = {divide(10, 2)}")

if __name__ == "__main__":
    main()
