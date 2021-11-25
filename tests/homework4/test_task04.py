import os
import pathlib

import pytest

from homework4.task_4_doctest import fizzbuzz


def test_string_input():
    """Testing program with wrong input data type"""
    with pytest.raises(ValueError):
        fizzbuzz('t')


def test_negative_input():
    """Testing program with wrong input data type"""
    with pytest.raises(ValueError):
        fizzbuzz(-3)


def test_fizzbuzz_number_case():
    """Testing when number in sequence is fizz and buzz simultaneously"""
    test_result = fizzbuzz(15)
    assert test_result.count('fizzbuzz') == 1
    assert test_result.count('fizz') == 4
    assert test_result.count('buzz') == 2


def test_docstring_tests():
    """Run fizzbuzz doctests from python code"""
    current_dir = pathlib.Path(__file__).resolve().parents[2]
    test_dir = os.path.join(current_dir, 'homework4', 'task_4_doctest.py')

    exit_code = pytest.main(['--doctest-modules', test_dir])

    assert exit_code == 0
