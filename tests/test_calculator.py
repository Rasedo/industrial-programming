import pytest

from app.calculator import calculate_value


def test_calculate_add():
    assert calculate_value(10, 5, 'add') == 15


def test_calculate_div():
    assert calculate_value(10, 2, 'div') == 5


# Представим, что мы изменили калькулятор, и он делает
# raise ValueError("Division by zero")
def test_calculate_div_by_zero():
    with pytest.raises(ValueError, match="Division by zero"):
        calculate_value(10, 0, 'div')
