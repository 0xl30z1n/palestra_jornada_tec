import calc_func
import pytest

NUMBER_1 = 3.0
NUMBER_2 = 2.0


def test_add():
    value = calc_func.add(NUMBER_1, NUMBER_2)
    assert value == 5.0


def test_subtract():
    # value = subtract(NUMBER_1, NUMBER_2)
    value = calc_func.subtract(NUMBER_1, NUMBER_2)
    assert value == 1.0


def test_subtract_negative():
    # value = subtract(NUMBER_2, NUMBER_1)
    value = calc_func.subtract(NUMBER_2, NUMBER_1)
    assert value == -1.0


def test_multiply():
    # value = multiply(NUMBER_1, NUMBER_2)
    value = calc_func.multiply(NUMBER_1, NUMBER_2)
    assert value == 6.0


def test_divide():
    # value = divide(NUMBER_1, NUMBER_2)
    value = calc_func.divide(NUMBER_1, NUMBER_2)
    assert value == 1.5


# Test for dividing by zero catches the exception
# https://docs.pytest.org/en/latest/how-to/assert.html

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        # divide(NUMBER_1, 0)
        calc_func.divide(NUMBER_1, 0)
    assert "division by zero" in str(e.value)


# Tests for maximum and minimum use parameters
# https://docs.pytest.org/en/latest/how-to/parametrize.html

@pytest.mark.parametrize("a,b,expected", [
    (NUMBER_1, NUMBER_2, NUMBER_1),
    (NUMBER_2, NUMBER_1, NUMBER_1),
    (NUMBER_1, NUMBER_1, NUMBER_1),
])
def test_maximum(a, b, expected):
    # assert maximum(a, b) == expected
    assert calc_func.maximum(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (NUMBER_1, NUMBER_2, NUMBER_2),
    (NUMBER_2, NUMBER_1, NUMBER_2),
    (NUMBER_2, NUMBER_2, NUMBER_2),
])
def test_minimum(a, b, expected):
    # assert minimum(a, b) == expected
    assert calc_func.minimum(a, b) == expected