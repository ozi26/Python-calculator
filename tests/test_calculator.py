# tests/test_calculator.py
import os
import sys


# Ensure the repository root is on sys.path so tests can import modules from repo root
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
sys.path.insert(0, ROOT)


from calculator import add, subtract, multiply, divide




def test_add():
assert add(2, 3) == 5




def test_subtract():
assert subtract(5, 2) == 3




def test_multiply():
assert multiply(3, 4) == 12




def test_divide():
assert divide(10, 2) == 5




def test_divide_by_zero_returns_error_string_or_raises():
r = divide(1, 0)
# Accept either handled string or an exception (depending on implementation choice)
assert r == "Error! Division by zero." or isinstance(r, Exception)
