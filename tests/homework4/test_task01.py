import pytest

from homework4.task_1_read_file import read_magic_number


def test_path_not_exists_case():
    """Testing function work if path is not exists"""
    dummy_path = 'dummy_path'

    with pytest.raises(ValueError):
        read_magic_number(dummy_path)


def test_first_line_not_a_number_case(tmpdir):
    """
    Testing when the first line of text file
    consists of not a number
    """
    test_text = 'fadhsaoi\n'
    tmp_path = tmpdir.mkdir("sub").join("tmp_text.txt")
    tmp_path.write(test_text)

    with pytest.raises(ValueError):
        read_magic_number(tmp_path)


def test_number_in_interval(tmpdir):
    """Testing when the first line consist of a number from interval [1, 3)"""
    test_text = '2\n'
    tmp_path = tmpdir.mkdir("sub").join("tmp_text.txt")
    tmp_path.write(test_text)

    assert read_magic_number(tmp_path)


def test_number_not_in_interval(tmpdir):
    """
    Testing when the first line consist of a number
    not from interval [1, 3)
    """
    test_text = '10\n'
    tmp_path = tmpdir.mkdir("sub").join("tmp_text.txt")
    tmp_path.write(test_text)

    assert not read_magic_number(tmp_path)
