"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.

You may assume that that every list contain at least one element

Example:

assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from typing import List, Any


def combinations(*args: List[Any]) -> List[List]:
    """
    Return all possible combinations of lists ordered by its elements entry
    """
    if len(args) == 1:
        return [*args]

    combinations_list = []
    result = [[]]
    for pool in args:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        combinations_list.append(prod)

    return combinations_list
