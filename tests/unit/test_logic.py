from calculadora.logic import add, subtract, multiply, divide
import pytest

def test_add():
    result = add(2, 2)
    print(f"[unit] ADD: 2 + 2 = {result}")
    assert result == 4
    result = add(-1, 1)
    print(f"[unit] ADD: -1 + 1 = {result}")
    assert result == 0

def test_subtract():
    result = subtract(10, 5)
    print(f"[unit] SUBTRACT: 10 - 5 = {result}")
    assert result == 5
    result = subtract(5, 10)
    print(f"[unit] SUBTRACT: 5 - 10 = {result}")
    assert result == -5

def test_multiply():
    result = multiply(3, 4)
    print(f"[unit] MULTIPLY: 3 * 4 = {result}")
    assert result == 12
    result = multiply(-2, 5)
    print(f"[unit] MULTIPLY: -2 * 5 = {result}")
    assert result == -10

def test_divide():
    result = divide(10, 2)
    print(f"[unit] DIVIDE: 10 / 2 = {result}")
    assert result == 5
    result = divide(-10, 2)
    print(f"[unit] DIVIDE: -10 / 2 = {result}")
    assert result == -5

def test_divide_by_zero():
    print("[unit] DIVIDE: 10 / 0 -> ValueError expected")
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
