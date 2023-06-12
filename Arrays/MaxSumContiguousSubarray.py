"""
    Find the maximum sum of contiguous non-empty subarray within an array A of length N.
"""
import sys


def max_sum_sub_array(arr):
    cur_sum, ans = 0, -sys.maxsize
    for num in arr:
        cur_sum += num
        ans = max(ans, cur_sum)
        if cur_sum < 0:
            cur_sum = 0
    return ans


print(max_sum_sub_array([1, 2, 3, 4, -10]))
print(max_sum_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
