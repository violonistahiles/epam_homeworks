from homework3.task04 import (get_digits_number, get_digits_power_sum, get_sum,
                              is_armstrong)


def test_get_digits_number():
    """Testing function works ok"""
    test_number = 42
    assert get_digits_number(test_number) == 2


def test_get_digits_number_with_zero():
    """Testing function works ok with zero as argument"""
    test_number = 0
    assert get_digits_number(test_number) == 1


def test_get_digits_power_sum():
    """Testing function works ok"""
    test_number = 42
    assert get_digits_power_sum(test_number) == 20


def test_get_digits_power_sum_with_zero():
    """Testing function works ok with zero as argument"""
    test_number = 0
    assert get_digits_power_sum(test_number) == 0


def test_get_sum():
    """Testing function works ok"""
    test_number = 42
    power = 2
    assert get_sum(test_number, power) == 20


def test_is_armstrong_when_number_is_armstrong():
    """Testing that Armstrong number is really Armstrong"""
    assert is_armstrong(407) is True


def test_is_armstrong_when_number_is_not_armstrong():
    """Testing that not Armstrong number is really not Armstrong"""
    assert is_armstrong(123) is False
