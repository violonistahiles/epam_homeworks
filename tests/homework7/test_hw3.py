from unittest.mock import Mock, patch

import pytest

from homework7.hw3 import (EmptyLineError, LineState, check_line, check_states,
                           get_line, get_states, tic_tac_toe_checker)


def test_check_line_x_wins_state():
    """
    Testing function return LineState instance with True
    in x_win attribute when only 'x' in list
    """
    dummy_type = 'some_type'
    dummy_board = [[]]
    mock = Mock(return_value=['x', 'x', 'x'])
    correct_state = LineState(True, False, False)

    with patch('homework7.hw3.get_line', mock):
        test_state = check_line(dummy_type, dummy_board)
        assert test_state == correct_state


def test_check_line_o_wins_state():
    """
    Testing function return LineState instance with True
    in o_win attribute when only 'o' in list
    """
    dummy_type = 'some_type'
    dummy_board = [[]]
    mock = Mock(return_value=['o', 'o', 'o'])
    correct_state = LineState(False, True, False)

    with patch('homework7.hw3.get_line', mock):
        test_state = check_line(dummy_type, dummy_board)
        assert test_state == correct_state


def test_check_line_unfinished():
    """
    Testing function return LineState instance with True
    in unfinished attribute when there is '-' in list
    """
    dummy_type = 'some_type'
    dummy_board = [[]]
    mock = Mock(return_value=['-', 'x', 'o'])
    correct_state = LineState(False, False, True)

    with patch('homework7.hw3.get_line', mock):
        test_state = check_line(dummy_type, dummy_board)
        assert test_state == correct_state


def test_get_line_horizontal():
    """
    Testing function return horizontal line with specified index from board
    """
    line_type = 'horizontal'
    test_board = [['-', '-', 'o'],
                  ['-', 'o', 'o'],
                  ['x', 'x', 'x']]
    index = 1
    correct_result = ['-', 'o', 'o']

    test_result = get_line(line_type, test_board, index)

    assert test_result == correct_result


def test_get_line_vertical():
    """
    Testing function return vertical line with specified index from board
    """
    line_type = 'vertical'
    test_board = [['-', '-', 'o'],
                  ['-', 'o', 'o'],
                  ['x', 'x', 'x']]
    index = 1
    correct_result = ['-', 'o', 'x']

    test_result = get_line(line_type, test_board, index)

    assert test_result == correct_result


def test_get_line_positive_diagonal():
    """
    Testing function return positive diagonal with from board
    """
    line_type = 'positive_diagonal'
    test_board = [['-', '-', 'o'],
                  ['-', 'o', 'o'],
                  ['x', 'x', 'x']]
    correct_result = ['-', 'o', 'x']

    test_result = get_line(line_type, test_board)

    assert test_result == correct_result


def test_get_line_negative_diagonal():
    """
    Testing function return negative diagonal with from board
    """
    line_type = 'negative_diagonal'
    test_board = [['-', '-', 'o'],
                  ['-', 'o', 'o'],
                  ['x', 'x', 'x']]
    correct_result = ['o', 'o', 'x']

    test_result = get_line(line_type, test_board)

    assert test_result == correct_result


def test_get_line_wrong_line_type():
    """
    Testing function raise error when wrong line type is passed
    """
    line_type = 'wrong_line_type'
    test_board = [['-', '-', 'o'],
                  ['-', 'o', 'o'],
                  ['x', 'x', 'x']]

    with pytest.raises(EmptyLineError):
        _ = get_line(line_type, test_board)


def test_check_state_x_win():
    """
    Testing function return "x wins!" if any of x_win states are True
    """
    state_one = LineState(True, False, False)
    state_two = LineState(False, True, True)
    state_three = LineState(False, False, False)
    test_states = [state_one, state_two, state_three]
    correct_result = 'x wins!'

    test_result = check_states(test_states)

    assert test_result == correct_result


def test_check_state_o_win():
    """
    Testing function return "o wins!" if any of o_win states are True
    """
    state_one = LineState(False, False, False)
    state_two = LineState(False, True, True)
    state_three = LineState(False, False, False)
    test_states = [state_one, state_two, state_three]
    correct_result = 'o wins!'

    test_result = check_states(test_states)

    assert test_result == correct_result


def test_check_state_unfinished():
    """
    Testing function return "unfinished!" if any of unfinished states are True
    """
    state_one = LineState(False, False, False)
    state_two = LineState(False, False, True)
    state_three = LineState(False, False, True)
    test_states = [state_one, state_two, state_three]
    correct_result = 'unfinished!'

    test_result = check_states(test_states)

    assert test_result == correct_result


def test_check_state_draw():
    """
    Testing function return "draw!" when there are no positive
    x_win, o_win, unfinished states
    """
    state_one = LineState(False, False, False)
    state_two = LineState(False, False, False)
    state_three = LineState(False, False, False)
    test_states = [state_one, state_two, state_three]
    correct_result = 'draw!'

    test_result = check_states(test_states)

    assert test_result == correct_result


def test_get_states():
    """Testing get_states invoked only 8 times"""
    dummy_board = [[]]
    mock = Mock(return_value=1)

    with patch('homework7.hw3.check_line', mock):
        test_result = get_states(dummy_board)
        assert sum(test_result) == 8


def test_tic_tac_toe_checker():
    """Testing get_states invoked only 8 times"""
    dummy_board = [[]]
    mock_one = Mock(return_value='some_states')
    mock_two = Mock(return_value='test_result')
    correct_result = 'test_result'

    with patch('homework7.hw3.get_states', mock_one), \
            patch('homework7.hw3.check_states', mock_two):
        test_result = tic_tac_toe_checker(dummy_board)
        assert test_result == correct_result
