"""
    Given an integer array A of size N. In one second, you can increase the value of one element by 1.
    Find the minimum time in seconds to make all elements of the array equal.
"""


def time_to_equality(arr):
    cur_max, cur_sum, n = arr[0], 0, len(arr)
    for num in arr:
        cur_sum += num
        if num > cur_max:
            cur_max = num
    return n * cur_max - cur_sum


print(time_to_equality([2, 4, 1, 3, 2]))
