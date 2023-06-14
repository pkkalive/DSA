"""
    You are given an integer array C of size A. Now you need to find a subarray (contiguous elements) so that the sum of contiguous elements is maximum.
    But the sum must not exceed B.
"""


def max_sub_array_sum(arr, target_sum):
    cur_sum, ans, index = 0, 0, 0
    for num in arr:
        cur_sum += num
        while cur_sum > target_sum:
            cur_sum -= arr[index]
            index += 1
        ans = max(ans, cur_sum)

    return ans


print(max_sub_array_sum([2, 1, 3, 4, 5], 12))
