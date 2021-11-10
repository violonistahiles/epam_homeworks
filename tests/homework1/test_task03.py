from unittest import mock
from homework1.task03 import find_maximum_and_minimum


def test_standard_case():
    """
    Testing that from text file minimum
    and maximum value returns correctly
    """
    some_string = '3\n1\n2\n3\n4'
    dummy_path = 'Z://dummy'
    correct_value = (1, 4)
    mock_open = mock.mock_open(read_data=some_string)

    with mock.patch('homework1.task03.open', mock_open) as m:
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

    with mock.patch('homework1.task03.open', mock_open) as m:
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

    with mock.patch('homework1.task03.open', mock_open) as m:
        test_result = find_maximum_and_minimum(dummy_path)

    assert test_result == correct_value
