import pytest

from task1.solution import strict


@strict
def sum_two(a: int, b: int) -> int:
    '''Сложение двух целых'''
    return a + b


@strict
def concat(a: str, b: str) -> str:
    '''Склейка двух строк'''
    return a + b


@strict
def divide(a: float, b: float) -> float:
    '''Деление двух чисел с плавающей точкой'''
    return a / b


@strict
def is_weekend(flag: bool) -> bool:
    '''Проверка булевого флага'''
    return flag


def test_addition_with_valid_ints():
    '''Успешное сложение int'''
    assert sum_two(42, 8) == 50
    assert sum_two(-3, 3) == 0


def test_string_concatenation_success():
    '''Успешная конкатенация строк'''
    assert concat('foo', 'bar') == 'foobar'
    assert concat('🔥', '🐍') == '🔥🐍'


def test_float_division_success():
    '''Успешное деление float'''
    assert divide(9.0, 3.0) == 3.0
    assert divide(5.5, 2.2) == 2.5


def test_boolean_handling_success():
    '''Успешная проверка булевых значений'''
    assert is_weekend(True) is True
    assert is_weekend(False) is False


def test_addition_type_error():
    '''Ошибка типа в сложении'''
    with pytest.raises(TypeError):
        sum_two(1, 25.5)
    with pytest.raises(TypeError):
        sum_two(1.1, 2)


def test_string_concat_type_error():
    '''Ошибка типа в конкатенации'''
    with pytest.raises(TypeError):
        concat('string', 123)
    with pytest.raises(TypeError):
        concat(52, 'string')


def test_float_division_type_error():
    '''Ошибка типа в делении'''
    with pytest.raises(TypeError):
        divide(9, 3.0)
    with pytest.raises(TypeError):
        divide(10, True)


def test_bool_argument_type_error():
    '''Ошибка типа для булевого аргумента'''
    with pytest.raises(TypeError):
        is_weekend('yes')
    with pytest.raises(TypeError):
        is_weekend(1)
