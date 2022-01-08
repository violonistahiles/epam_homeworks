from unittest.mock import Mock, patch

import pytest

from homework7.hw1 import (NotDictError, compare_element, find_occurrences,
                           process_branch, process_value)


def test_compare_element_int():
    """Testing compare_element works correct with int data type"""
    element = 1
    element_to_compare = 1

    assert compare_element(element, element_to_compare)


def test_compare_element_str():
    """Testing compare_element works correct with str data type"""
    element = 'a'
    element_to_compare = 'a'

    assert compare_element(element, element_to_compare)


def test_compare_element_bool():
    """Testing compare_element works correct with bool data type"""
    element = True
    element_to_compare = True

    assert compare_element(element, element_to_compare)


def test_compare_element_set():
    """Testing compare_element works correct with set data type"""
    element = {1, 4, 5}
    element_to_compare = {1, 4, 5}

    assert compare_element(element, element_to_compare)


def test_compare_element_list():
    """Testing compare_element works correct with list data type"""
    element = [1, 4, 5]
    element_to_compare = [1, 4, 5]

    assert compare_element(element, element_to_compare)


def test_compare_element_tuple():
    """Testing compare_element works correct with tuple data type"""
    element = (1, 4, 5)
    element_to_compare = (1, 4, 5)

    assert compare_element(element, element_to_compare)


def test_compare_element_dict():
    """Testing compare_element works correct with dict data type"""
    element = {1: 2, 'a': 'b'}
    element_to_compare = {1: 2, 'a': 'b'}

    assert compare_element(element, element_to_compare)


def test_compare_element_wrong_data_type():
    """Testing compare_element raise error with unsupported data type"""
    element = {1: 2, 'a': 'b'}
    element_to_compare = object()

    with pytest.raises(ValueError):
        compare_element(element, element_to_compare)


def test_compare_element_different_values():
    """Testing compare_element return 0 with different values"""
    element = {1: 2, 'a': 'b'}
    element_to_compare = 25

    assert not compare_element(element, element_to_compare)


def test_process_value_elements_with_equal_data_type():
    """
    Testing process_value invoke compare_element only once with
    equal value and element
    """
    element = {1: 2, 'a': 'b'}
    element_to_compare = {1: 2, 'a': 'b'}
    mock = Mock(return_value=1)

    with patch('homework7.hw1.compare_element', mock) as mock_ce:
        assert process_value(element, element_to_compare)
        mock_ce.assert_called_once()


def test_process_value_elements_with_different_data_type_but_value_not_dict():
    """
    Testing process_value invoke process_branch only once with
    different value and element
    """
    element = {5, 2, 5}
    element_to_compare = 12

    def return_one(*args):
        return 1

    with patch('homework7.hw1.process_branch', return_one):
        test_result = process_value(element, element_to_compare)
        assert test_result == 1


def test_process_value_elements_with_equal_data_type_but_different_value():
    """
    Testing process_value with equal input data type but different value
    invoke process_branch only and compare_element once
    """
    element = {1: 2, 'a': 'b'}
    element_to_compare = {1: 2, 'a': 'c'}
    mock = Mock(return_value=0)

    def return_one(*args):
        return 1

    with patch('homework7.hw1.compare_element', mock) as mock_ce, \
            patch('homework7.hw1.process_branch', return_one):
        test_result = process_value(element, element_to_compare)
        assert test_result == 1
        mock_ce.assert_called_once()


def test_process_branch_with_iterable_input():
    """
    Testing process_branch invoke process_value
    times equal to branch length
    """
    test_branch = [1, 2, 'ads']
    element_to_compare = 25
    correct_result = len(test_branch)
    mock = Mock(return_value=1)

    with patch('homework7.hw1.process_value', mock):
        test_result = process_branch(test_branch, element_to_compare)
        assert test_result == correct_result


def test_process_branch_with_non_iterable_input():
    """
    Testing process_branch invoke process_value
    times equal to branch length
    """
    test_tree = 5
    element_to_compare = 25
    mock = Mock(return_value=1)

    with patch('homework7.hw1.compare_element', mock) as mock_ce:
        assert process_branch(test_tree, element_to_compare)
        mock_ce.assert_called_once()


def test_find_occurrences_input_tree_dict():
    """
    Testing find_occurrences invoke
    process_value times equal to tree length
    """
    test_tree = {1: 2, 'a': 'b', (1, 'a'): 'c'}
    element_to_compare = 25
    correct_result = 6
    mock = Mock(return_value=1)

    with patch('homework7.hw1.process_value', mock):
        test_result = find_occurrences(test_tree, element_to_compare)
        assert test_result == correct_result


def test_find_occurrences_input_tree_not_dict():
    """Testing find_occurrences raise error when tree is not a dict"""
    test_branch = [1, 2, 3]
    element_to_compare = 25

    with pytest.raises(NotDictError):
        _ = find_occurrences(test_branch, element_to_compare)
