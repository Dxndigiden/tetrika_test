import pytest
from task1.solution import strict


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


@strict
def concat(a: str, b: str) -> str:
    return a + b


@strict
def divide(a: float, b: float) -> float:
    return a / b


@strict
def is_weekend(flag: bool) -> bool:
    return flag


# Удачные случаи
def test_addition_with_valid_ints():
    assert sum_two(42, 8) == 50
    assert sum_two(-3, 3) == 0


def test_string_concatenation_success():
    assert concat('foo', 'bar') == 'foobar'
    assert concat('🔥', '🐍') == '🔥🐍'


def test_float_division_success():
    assert divide(9.0, 3.0) == 3.0
    assert divide(5.5, 2.2) == 2.5


def test_boolean_handling_success():
    assert is_weekend(True) is True
    assert is_weekend(False) is False


# Ошибки типов
def test_addition_type_error():
    with pytest.raises(TypeError):
        sum_two(1, 25.5)

    with pytest.raises(TypeError):
        sum_two(1.1, 2)


def test_string_concat_type_error():
    with pytest.raises(TypeError):
        concat('string', 123)

    with pytest.raises(TypeError):
        concat(52, 'string')


def test_float_division_type_error():
    with pytest.raises(TypeError):
        divide(9, 3.0)

    with pytest.raises(TypeError):
        divide(10, True)


def test_bool_argument_type_error():
    with pytest.raises(TypeError):
        is_weekend('yes')

    with pytest.raises(TypeError):
        is_weekend(1)
