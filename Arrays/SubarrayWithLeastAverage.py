"""
    Given an array of size N, find the subarray of size K with the least average.
"""
import sys


def least_sub_array_avg(arr, k):
    n, ans, cur_sum, index = len(arr), sys.maxsize, 0, 0
    for i in range(k):
        cur_sum += arr[i]

    ans = min(ans, cur_sum)
    for i in range(k, n):
        cur_sum += arr[i]
        cur_sum -= arr[i - k]
        if cur_sum < ans:
            ans = cur_sum
            index = i - k + 1
    return index


print(least_sub_array_avg([3, 7, 90, 20, 10, 50, 40], 3))
print(least_sub_array_avg([3, 7, 5, 20, -10, 0, 12], 2))
