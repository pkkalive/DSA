"""
    Given an array A of N non-negative numbers and a non-negative number B, you need to find the number of sub-arrays in A with a sum less than B. We may assume that there is no overflow.
"""


def count_sub_arrays(arr, k):
    n = len(arr)
    cur_sum, left_index, count = 0, 0, 0
    for cur_index in range(n):
        cur_sum += arr[cur_index]
        while cur_sum >= k:
            cur_sum -= arr[left_index]
            left_index += 1
        count += cur_index - left_index + 1
    return count


print(count_sub_arrays([1, 2, 3], 10))
print(count_sub_arrays([2, 5, 6], 10))
print(count_sub_arrays([1, 11, 2, 3, 15], 10))
