"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
from collections import Counter
from typing import List, Tuple, Union


def major_and_minor_elem(inp: List) -> Union[None, Tuple[int, int]]:
    """Find major and minor element from array"""
    if len(inp) <= 2:
        return None

    list_counter = Counter(inp)
    counted_elements = list_counter.most_common()

    return counted_elements[0][0], counted_elements[-1][0]
