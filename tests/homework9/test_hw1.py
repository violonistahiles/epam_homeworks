import pytest

from homework9.hw1 import merge_sorted_files


def test_all_files_with_integers(tmpdir):
    """Testing merge_sorted_files merges integers from file in right order"""
    text_1 = '1\n3\n5'
    text_2 = '2\n4\n6'
    path_1 = tmpdir.mkdir('sub_1').join('test_text_1.txt')
    path_1.write(text_1)
    path_2 = tmpdir.mkdir('sub_2').join('test_text_2.txt')
    path_2.write(text_2)
    paths = [path_1, path_2]
    correct_result = [1, 2, 3, 4, 5, 6]

    test_result = list(merge_sorted_files(paths))

    assert test_result == correct_result


def test_some_file_with_wrong_data_type(tmpdir):
    """
    Testing ValueError is raised if data
    in file line cant be converted to integer
    """
    text_1 = '1\n3\n5'
    text_2 = '2\n4\nwrong_data_type'
    path_1 = tmpdir.mkdir('sub_1').join('test_text_1.txt')
    path_1.write(text_1)
    path_2 = tmpdir.mkdir('sub_2').join('test_text_2.txt')
    path_2.write(text_2)
    paths = [path_1, path_2]

    with pytest.raises(ValueError):
        _ = list(merge_sorted_files(paths))


def test_files_are_empty(tmpdir):
    """Testing empty files are processing correctly"""
    text_1 = ''
    text_2 = ''
    path_1 = tmpdir.mkdir('sub_1').join('test_text_1.txt')
    path_1.write(text_1)
    path_2 = tmpdir.mkdir('sub_2').join('test_text_2.txt')
    path_2.write(text_2)
    paths = [path_1, path_2]

    correct_result = []

    test_result = list(merge_sorted_files(paths))

    assert test_result == correct_result


def test_two_files_are_empty(tmpdir):
    """Testing that empty files are not influence on program process"""
    text_1 = '1\n3\n5'
    text_2 = ''
    text_3 = '2\n4\n6\n7\n'
    text_4 = ''
    path_1 = tmpdir.mkdir('sub_1').join('test_text_1.txt')
    path_1.write(text_1)
    path_2 = tmpdir.mkdir('sub_2').join('test_text_2.txt')
    path_2.write(text_2)
    path_3 = tmpdir.mkdir('sub_3').join('test_text_3.txt')
    path_3.write(text_3)
    path_4 = tmpdir.mkdir('sub_4').join('test_text_4.txt')
    path_4.write(text_4)
    paths = [path_1, path_2, path_3, path_4]

    correct_result = [1, 2, 3, 4, 5, 6, 7]

    test_result = list(merge_sorted_files(paths))

    assert test_result == correct_result
