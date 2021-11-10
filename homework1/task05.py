"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:

    nums_len = len(nums)
    if k > nums_len:
        k = nums_len
    elif k == 1:
        return max(nums)
    elif k < 0:
        return None

    if nums_len == 0:
        return None
    elif nums_len == 1:
        return nums[0]

    max_sum_index_start = 0
    max_sum_index_end = 1
    max_sum = sum(nums[max_sum_index_start:max_sum_index_end])
    for i in range(1, k+1):
        for j in range(nums_len-i+1):
            current_sum = sum(nums[j:j+i])
            if current_sum > max_sum:
                max_sum = current_sum
                max_sum_index_start = j
                max_sum_index_end = j + i

    result = sum(nums[max_sum_index_start:max_sum_index_end])

    return result
