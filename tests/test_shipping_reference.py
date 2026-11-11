
import pytest

from data.sample_code.shipping import (
    calculate_shipping,
    is_free_shipping
)


def test_domestic_light_package():
    assert calculate_shipping(3, "domestic") == 5


def test_domestic_heavy_package():
    assert calculate_shipping(8, "domestic") == 10


def test_international_light_package():
    assert calculate_shipping(3, "international") == 15


def test_international_heavy_package():
    assert calculate_shipping(8, "international") == 25


def test_domestic_express_shipping():
    assert calculate_shipping(3, "domestic", express=True) == 15


def test_international_express_shipping():
    assert calculate_shipping(8, "international", express=True) == 35


def test_pickup_is_free():
    assert calculate_shipping(3, "pickup") == 0


def test_zero_weight_raises_exception():
    with pytest.raises(ValueError, match="Weight must be positive"):
        calculate_shipping(0, "domestic")


def test_negative_weight_raises_exception():
    with pytest.raises(ValueError, match="Weight must be positive"):
        calculate_shipping(-2, "domestic")


def test_invalid_destination_raises_exception():
    with pytest.raises(ValueError, match="Invalid destination"):
        calculate_shipping(3, "unknown")


def test_pickup_is_free_shipping():
    assert is_free_shipping(3, "pickup") is True


def test_domestic_is_not_free_shipping():
    assert is_free_shipping(3, "domestic") is False
