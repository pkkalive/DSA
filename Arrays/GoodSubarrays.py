"""
    Given an array of integers A, a subarray of an array is said to be good if it fulfills any one of the criteria:
    1. Length of the subarray is even, and the sum of all the elements of the subarray must be less than B.
    2. Length of the subarray is odd, and the sum of all the elements of the subarray must be greater than B.
    Your task is to find the count of good sub-arrays in A.
"""


def good_sub_arrays(arr, k):
    n, count = len(arr), 0
    prefix_sum, cur_sum = [], 0
    for num in arr:
        cur_sum += num
        prefix_sum.append(cur_sum)

    for i in range(n):
        for j in range(i, n):
            size = j - i + 1
            cur_sum = 0
            if i == 0:
                cur_sum = prefix_sum[j]
            else:
                cur_sum = prefix_sum[j] - prefix_sum[i - 1]
            if cur_sum > k and size & 1 == 1:
                count += 1
            if cur_sum < k and size & 1 == 0:
                count += 1
    return count


print(good_sub_arrays([1, 2, 3, 4, 5], 4))
print(good_sub_arrays([13, 16, 16, 15, 9, 16, 2, 7, 6, 17, 3, 9], 65))
