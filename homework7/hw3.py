"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from typing import List

# Sentinel object
empty_element = object()


class EmptyLineError(Exception):
    """Handle exceptions related to board values"""


class LineState:
    """Store states of one line from board"""
    def __init__(self, x_win: bool, o_win: bool, unfinished: bool) -> None:
        self.x_win = x_win
        self.o_win = o_win
        self.unfinished = unfinished

    def __eq__(self, other):
        attributes_to_check = ['x_win', 'o_win', 'unfinished']
        for attribute in attributes_to_check:
            if self.__dict__[attribute] != other.__dict__[attribute]:
                return False
        return True


def check_line(line_type: str, board: List[List], index: int = 0) -> LineState:
    """Collect states from one line on board"""
    list_to_check = get_line(line_type, board, index)
    x_win = all([cell == 'x' for cell in list_to_check])
    o_win = all([cell == 'o' for cell in list_to_check])
    unfinished = bool('-' in list_to_check)

    state = LineState(x_win, o_win, unfinished)
    return state


def get_line(line_type: str, board: List[List], index: int = 0) -> List[str]:
    """Define elements from board for current line"""
    list_to_check = empty_element  # sentinel

    if line_type == 'horizontal':
        list_to_check = board[index]

    if line_type == 'vertical':
        list_to_check = [cell[index] for cell in board]

    # From top left to bottom right
    if line_type == 'positive_diagonal':
        list_to_check = [board[i][i] for i in range(3)]

    # From bottom left to top right
    if line_type == 'negative_diagonal':
        list_to_check = [board[i][2-i] for i in range(3)]

    if list_to_check == empty_element:
        raise EmptyLineError('Board line is empty')

    return list_to_check


def check_states(states: List[LineState]) -> str:
    """Check conditions for all possible game states"""
    if any([state.x_win for state in states]):
        return 'x wins!'

    if any([state.o_win for state in states]):
        return 'o wins!'

    if any([state.unfinished for state in states]):
        return 'unfinished!'

    return 'draw!'


def get_states(board: List[List]) -> List[LineState]:
    """Process all possible game states"""
    states = list()
    states.append(check_line('positive_diagonal', board))
    states.append(check_line('negative_diagonal', board))

    for line_index in range(3):
        states.append(check_line('horizontal', board, line_index))
        states.append(check_line('vertical', board, line_index))

    return states


def tic_tac_toe_checker(board: List[List]) -> str:
    """Check current game state for 3x3 tic tac toe game"""
    board_states = get_states(board)
    result = check_states(board_states)
    return result
