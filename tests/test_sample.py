import pytest

from examples.improved_sample import calculate_average


def test_calculate_average():
    assert calculate_average([80, 90, 75]) == pytest.approx(81.6666667)


def test_calculate_average_single_value():
    assert calculate_average([50]) == 50


def test_calculate_average_empty_list():
    with pytest.raises(ValueError):
        calculate_average([])
