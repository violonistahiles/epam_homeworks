import pytest

from homework4.task_5_optional import fizzbuzz


def test_string_input():
    """Testing program with wrong input data type"""
    with pytest.raises(ValueError):
        list(fizzbuzz('t'))


def test_negative_input():
    """Testing program with wrong input data type"""
    with pytest.raises(ValueError):
        list(fizzbuzz(-3))


def test_fizzbuzz_number_case():
    """Testing when number in sequence is fizz and buzz simultaneously"""
    test_result = list(fizzbuzz(15))
    assert test_result.count('fizzbuzz') == 1
    assert test_result.count('fizz') == 4
    assert test_result.count('buzz') == 2
