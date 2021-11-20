"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
compute how many tuples (i, j, k, l) there are
such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from collections import defaultdict
from itertools import product
from typing import List


def check_sum_of_four(a: List[int],
                      b: List[int],
                      c: List[int],
                      d: List[int]) -> int:
    """
    Compute how many tuples (i, j, k, l) there are
    such that A[i] + B[j] + C[k] + D[l] is zero
    """
    # Get subset of sums from first two lists
    sub_sum_1 = defaultdict(int)
    for prod in product(a, b):
        sub_sum_1[-1*sum(prod)] += 1

    # Get subset of sums from second two lists
    # And process sums only from first sub_sum set
    valid_sums = set()
    sub_sum_2 = defaultdict(int)
    for prod in product(c, d):
        prod_sum = sum(prod)
        if prod_sum in sub_sum_1:
            valid_sums.update([prod_sum])
            sub_sum_2[prod_sum] += 1

    result = 0
    for sum_value in valid_sums:
        result += sub_sum_1[sum_value] * sub_sum_2[sum_value]

    return result
