from homework2.hw2 import major_and_minor_elem


def test_standard_case_example_1():
    """Testing algorithm on standard input"""
    test_list = [3, 2, 3]
    correct_result = 3, 2

    result = major_and_minor_elem(test_list)

    assert result == correct_result


def test_standard_case_example_2():
    """Testing algorithm on standard input"""
    test_list = [2, 2, 1, 1, 1, 2, 2]
    correct_result = 2, 1

    result = major_and_minor_elem(test_list)

    assert result == correct_result


def test_list_with_one_unique_element():
    """Testing algorithm result on list with one unique element"""
    test_list = [1, 1, 1]
    correct_result = 1, 1

    result = major_and_minor_elem(test_list)

    assert result == correct_result


def test_list_with_length_less_then_three():
    """Testing algorithm result on list with one unique element"""
    test_list = [1, 1]

    result = major_and_minor_elem(test_list)

    assert not result
