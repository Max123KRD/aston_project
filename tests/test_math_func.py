import pytest
from . import math_func


@pytest.mark.parametrize("num1, num2, result",
                         [
                             (7, 3, 10),
                             ("Hello", " World", "Hello World"),
                             (10.5, 25.5, 36)
                         ])
def test_add(num1, num2, result):
    assert math_func.add_func(num1, num2) == result


@pytest.mark.numbers
def test_mult_num():
    assert math_func.mult_func(7, 2) == 14
    assert math_func.mult_func(7) == 14


@pytest.mark.strings
def test_mult_str():
    assert math_func.mult_func("Hello ") == "Hello Hello "