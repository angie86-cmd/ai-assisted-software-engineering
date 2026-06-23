import pytest

from src.fibonacci import fibonacci


def test_zero():
    assert fibonacci(0) == []


def test_one():
    assert fibonacci(1) == [0]


def test_ten():
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_negative():
    with pytest.raises(ValueError):
        fibonacci(-5)


def test_non_integer():
    with pytest.raises(TypeError):
        fibonacci(2.5)
