from src.ai_validator import validate_generated_tests


def test_valid_generated_tests():

    code = """
import pytest

from data.sample_code.calculator import calculate_discount

def test_normal_discount():
    assert calculate_discount(100, 20) == 80
"""

    result = validate_generated_tests(code)

    assert result["valid_python"] is True
    assert result["contains_test_functions"] is True
    assert result["redefines_original_function"] is False
    assert result["contains_pytest"] is True


def test_detects_reimplemented_function():

    code = """
def calculate_discount(price, discount):
    return price
"""

    result = validate_generated_tests(code)

    assert result["redefines_original_function"] is True

def test_detects_pytest_main():

    code = """
import pytest

def test_example():
    assert 1 == 1

pytest.main()
"""

    result = validate_generated_tests(code)

    assert result["contains_pytest_main"] is True

def test_detects_original_function_import():

    code = """
import pytest
from data.sample_code.calculator import calculate_discount

def test_normal_discount():
    assert calculate_discount(100, 20) == 80
"""

    result = validate_generated_tests(code)

    assert result["imports_original_function"] is True
    assert result["safe_to_execute"] is True

def test_reimplemented_function_is_not_safe():

    code = """
import pytest

def calculate_discount(price, discount):
    return price

def test_discount():
    assert calculate_discount(100, 20) == 80
"""

    result = validate_generated_tests(code)

    assert result["redefines_original_function"] is True
    assert result["safe_to_execute"] is False


def get_shipping_source_code():
    return """
def calculate_shipping(weight, destination, express=False):
    return 5

def is_free_shipping(weight, destination):
    return False
"""


def test_accepts_correct_exception_handling():

    code = """
import pytest
from data.sample_code.shipping import calculate_shipping, is_free_shipping

def test_invalid_weight():
    with pytest.raises(ValueError):
        calculate_shipping(0, "domestic")
"""

    result = validate_generated_tests(
        code,
        "data.sample_code.shipping",
        ["calculate_shipping", "is_free_shipping"],
        get_shipping_source_code()
    )

    assert result["correct_exception_handling"] is True
    assert result["valid_function_calls"] is True
    assert result["safe_to_execute"] is True


def test_rejects_incorrect_exception_handling():

    code = """
import pytest
from data.sample_code.shipping import calculate_shipping, is_free_shipping

def test_invalid_weight():
    assert calculate_shipping(0, "domestic") == pytest.raises(ValueError)
"""

    result = validate_generated_tests(
        code,
        "data.sample_code.shipping",
        ["calculate_shipping", "is_free_shipping"],
        get_shipping_source_code()
    )

    assert result["correct_exception_handling"] is False
    assert result["safe_to_execute"] is False


def test_rejects_invalid_function_arguments():

    code = """
import pytest
from data.sample_code.shipping import calculate_shipping, is_free_shipping

def test_invalid_call():
    is_free_shipping(1, "domestic", express=True)
"""

    result = validate_generated_tests(
        code,
        "data.sample_code.shipping",
        ["calculate_shipping", "is_free_shipping"],
        get_shipping_source_code()
    )

    assert result["valid_function_calls"] is False
    assert result["safe_to_execute"] is False
