from typing import Any


def add(x: int, y: int) -> int:
    return x + y


def subtract(x: int, y: int) -> int:
    return x - y


def multiply(x: int, y: int) -> int:
    return x * y


def divide(x: int, y: int) -> float:
    try:
        return x / y
    except ZeroDivisionError:
        raise ValueError("Cannot divide by zero")


def power(base: int, exponent: int) -> Any:
    return pow(base, exponent)
