import pytest

from homework4.task_4_doctest import fizzbuzz


def test_string_input():
    """Testing program with wrong input data type"""
    with pytest.raises(ValueError):
        fizzbuzz('t')


def test_fizzbuzz_number_case():
    """Testing when number in sequence is fizz and buzz simultaneously"""
    test_result = fizzbuzz(15)
    assert 'fizzbuzz' in test_result
