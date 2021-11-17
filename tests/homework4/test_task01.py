import os
from unittest import mock

import pytest

from homework4.task_1_read_file import read_magic_number


# @pytest.fixture
# def wrong_text():
#     text = 'fsdsfsd\n'
#     with open(os.path.join(os.getcwd(), 'tests', 'test_text.txt'), 'w') as f:
#         f.write(text)
#
#
# @pytest.fixture
# def correct_text():
#     text = '2\n'
#     with open(os.path.join(os.getcwd(), 'tests', 'test_text.txt'), 'w') as f:
#         f.write(text)


def test_path_not_exists_case():
    """Testing function work if path is not exists"""
    dummy_path = 'dummy_path'

    with pytest.raises(ValueError):
        read_magic_number(dummy_path)


def test_can_not_convert_to_float():
    """
    Testing when the first line of text file
    consists of not a number
    """
    test_text = 'fadhsaoi\n'
    existed_path = os.getcwd()
    mock_open = mock.mock_open(read_data=test_text.encode('utf-8'))

    with mock.patch('homework4.task_1_read_file.open', mock_open):
        with pytest.raises(ValueError):
            read_magic_number(existed_path)


def test_number_between_one_and_three():
    """Testing when the first line consist of a number from interval [1, 3)"""
    test_text = '2\n'
    existed_path = os.getcwd()
    mock_open = mock.mock_open(read_data=test_text.encode('utf-8'))

    with mock.patch('homework4.task_1_read_file.open', mock_open):
        assert read_magic_number(existed_path)


def test_number_not_in_interval():
    """
    Testing when the first line consist of a number
    not from interval [1, 3)
    """
    test_text = '10\n'
    existed_path = os.getcwd()
    mock_open = mock.mock_open(read_data=test_text.encode('utf-8'))

    with mock.patch('homework4.task_1_read_file.open', mock_open):
        assert not read_magic_number(existed_path)
