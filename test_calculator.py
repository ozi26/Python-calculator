import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(5, 3) == 8
    assert add(-2, 2) == 0
    assert add(1.5, 2.5) == 4.0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-2, -2) == 0
    assert subtract(5, 7) == -2
    assert subtract(3.5, 1.5) == 2.0

def test_multiply():
    assert multiply(5, 3) == 15
    assert multiply(-2, 3) == -6
    assert multiply(0, 100) == 0
    assert multiply(2.5, 2) == 5.0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, 2) == 2.5
    assert divide(-10, 2) == -5
    assert divide(0, 5) == 0
    assert divide(10, 0) == "Error: Division by zero is not allowed."
