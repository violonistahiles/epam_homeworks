from unittest import mock

import pytest

from homework1.task03 import (NotIntError, find_maximum_and_minimum,
                              line_generator)


def test_line_generator_with_not_int_element():
    """Testing line generator work correct"""
    some_string = '3\n1\n2\nnot_int\n4'
    dummy_path = 'Z://dummy'
    mock_open = mock.mock_open(read_data=some_string)

    with mock.patch('homework1.task03.open', mock_open):
        with pytest.raises(NotIntError):
            _ = list(line_generator(dummy_path))


def test_line_generator():
    """Testing line generator work correct"""
    some_string = '3\n1\n2\n3\n4'
    dummy_path = 'Z://dummy'
    correct_value = [3, 1, 2, 3, 4]
    mock_open = mock.mock_open(read_data=some_string)

    with mock.patch('homework1.task03.open', mock_open):
        test_result = list(line_generator(dummy_path))

    assert test_result == correct_value


def test_standard_case():
    """
    Testing that from text file minimum
    and maximum value returns correctly
    """
    some_string = '3\n1\n2\n3\n4'
    dummy_path = 'Z://dummy'
    correct_value = (4, 1)
    mock_open = mock.mock_open(read_data=some_string)

    with mock.patch('homework1.task03.open', mock_open):
        test_result = find_maximum_and_minimum(dummy_path)

    assert test_result == correct_value


def test_all_integers_are_equal_case():
    """
    Testing that from text file when all integers are equal minimum
    and maximum value would be the same
    """
    some_string = '1\n1\n1\n1'
    dummy_path = 'Z://dummy'
    correct_value = (1, 1)
    mock_open = mock.mock_open(read_data=some_string)

    with mock.patch('homework1.task03.open', mock_open):
        test_result = find_maximum_and_minimum(dummy_path)

    assert test_result == correct_value


def test_one_integer_case():
    """
    Testing that from text file with one line minimum
    and maximum value would be the same
    """
    some_string = '5'
    dummy_path = 'Z://dummy'
    correct_value = (5, 5)
    mock_open = mock.mock_open(read_data=some_string)

    with mock.patch('homework1.task03.open', mock_open):
        test_result = find_maximum_and_minimum(dummy_path)

    assert test_result == correct_value
