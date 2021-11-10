"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
compute how many tuples (i, j, k, l) there are
such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List
from collections import defaultdict


def check_sum_of_four(a: List[int],
                      b: List[int],
                      c: List[int],
                      d: List[int]) -> int:

    def take_equal(first: List[int], second: List[int]) -> List[int]:
        """Select only equal elements from two lists"""

        def _take_equal():
            while first and second:
                value = (first if first[0] <= second[0] else second).pop(0)
                if len(first) > 0 and value == first[0]:
                    first.pop(0)
                    yield value

                if len(second) > 0 and value == second[0]:
                    second.pop(0)
                    yield value

        return list(_take_equal())

    # Divide sum of four elements to two sums of two elements
    # Get sums of the first two lists
    subset_ab = defaultdict(int)
    for i in range(len(a)):
        for j in range(len(b)):
            subset_ab[a[i] + b[j]] += 1
    ab_values = sorted(list(subset_ab.keys()))

    # Get sums of the second two lists with minus
    subset_cd = defaultdict(int)
    for i in range(len(c)):
        for j in range(len(d)):
            subset_cd[-(c[i] + d[j])] += 1
    cd_values = sorted(list(subset_cd.keys()))

    # Select only equal elements from two lists
    valid_values = take_equal(ab_values, cd_values)
    result = 0
    # According to the number of sum entries get final tuples number
    for key in valid_values:
        result += subset_cd[key] * subset_ab[key]

    return result
