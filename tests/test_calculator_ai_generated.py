
import pytest

from data.sample_code.calculator import calculate_discount


def test_normal_discount():
    assert calculate_discount(100, 20) == 80


def test_zero_discount():
    assert calculate_discount(100, 0) == 100


def test_full_discount():
    assert calculate_discount(100, 100) == 0


def test_zero_price():
    assert calculate_discount(0, 20) == 0


def test_negative_price():
    with pytest.raises(ValueError):
        calculate_discount(-100, 20)


def test_negative_discount():
    with pytest.raises(ValueError):
        calculate_discount(100, -10)


def test_discount_above_100():
    with pytest.raises(ValueError):
        calculate_discount(100, 120)
