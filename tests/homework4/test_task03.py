import pytest

from homework4.task_3_get_print_output import my_precious_logger


def test_error_message_case(capsys):
    """Testing what text witch starts with "error" in stderr"""
    test_text = 'error: file not found'

    my_precious_logger(test_text)
    captured = capsys.readouterr()

    assert captured.err == test_text + '\n'


def test_normal_message_case(capsys):
    """Testing what text witch starts not with "error" in stdout"""
    test_text = 'file not found'

    my_precious_logger(test_text)
    captured = capsys.readouterr()

    assert captured.out == test_text + '\n'


def test_input_is_not_a_string():
    """Testing when input is not a string"""
    test_text = 25

    with pytest.raises(ValueError):
        my_precious_logger(test_text)