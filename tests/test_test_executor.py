
from src.test_executor import execute_generated_tests


def test_execute_valid_generated_tests():

    code = """
import pytest
from data.sample_code.calculator import calculate_discount

def test_normal_discount():
    assert calculate_discount(100, 20) == 80

def test_zero_discount():
    assert calculate_discount(100, 0) == 100

def test_negative_price():
    with pytest.raises(ValueError):
        calculate_discount(-100, 20)
"""

    result = execute_generated_tests(code)

    assert result["success"] is True
    assert result["passed"] == 3
    assert result["failed"] == 0


def test_reject_reimplemented_function():

    code = """
import pytest

def calculate_discount(price, discount):
    return price

def test_discount():
    assert calculate_discount(100, 20) == 80
"""

    result = execute_generated_tests(code)

    assert result["success"] is False
    assert result["message"] == "Generated tests failed validation."
