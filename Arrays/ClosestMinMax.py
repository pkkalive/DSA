"""
    Given an array A, find the size of the smallest subarray such that it contains at least one occurrence of the maximum value of the array and at least one occurrence of the minimum value of the array.
"""
import sys


def closest_min_max(arr):
    n, ans = len(arr), sys.maxsize
    cur_min, cur_max = sys.maxsize, -sys.maxsize
    min_idx, max_idx = -1, -1
    for i in range(n):
        if arr[i] > cur_max:
            cur_max = arr[i]
        if arr[i] < cur_min:
            cur_min = arr[i]

    for i in range(n):
        if arr[i] == cur_min:
            min_idx = i
        if arr[i] == cur_max:
            max_idx = i
        if min_idx != -1 and max_idx != -1:
            ans = min(ans, abs(max_idx - min_idx) + 1)

    return ans


print(closest_min_max([814, 761, 697, 483, 981]))
