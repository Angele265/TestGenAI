
import pytest

from data.sample_code.shipping import (
    calculate_shipping,
    is_free_shipping
)


# Normal shipping scenarios

def test_domestic_light():
    assert calculate_shipping(1, "domestic") == 5


def test_domestic_heavy():
    assert calculate_shipping(6, "domestic") == 10


def test_international_light():
    assert calculate_shipping(1, "international") == 15


def test_international_heavy():
    assert calculate_shipping(6, "international") == 25


def test_pickup():
    assert calculate_shipping(1, "pickup") == 0


# Express shipping

def test_domestic_express():
    assert calculate_shipping(1, "domestic", express=True) == 15


def test_international_express():
    assert calculate_shipping(6, "international", express=True) == 35


# Invalid inputs

def test_zero_weight():
    with pytest.raises(ValueError):
        calculate_shipping(0, "domestic")


def test_negative_weight():
    with pytest.raises(ValueError):
        calculate_shipping(-1, "domestic")


def test_invalid_destination():
    with pytest.raises(ValueError):
        calculate_shipping(1, "invalid")


# Free shipping

def test_pickup_is_free():
    assert is_free_shipping(1, "pickup") is True


def test_domestic_is_not_free():
    assert is_free_shipping(1, "domestic") is False


def test_international_is_not_free():
    assert is_free_shipping(1, "international") is False


def test_zero_weight_free_shipping():
    with pytest.raises(ValueError):
        is_free_shipping(0, "domestic")

