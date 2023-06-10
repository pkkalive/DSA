"""
    You are given an integer array A of size N.
    You have to perform B operations. In one operation, you can remove either the leftmost or the rightmost element of the array A.
    Find and return the maximum possible sum of the elements that were removed after B operations.
    NOTE: Suppose B = 4, and array A contains 10 elements, then You can remove the first four elements or can remove the last four elements, or can remove 1 from front and 3 from the back,
    etc. You need to return the maximum possible sum of elements you can remove.
"""


def pick_from_both_sides(arr, k):
    n, cur_max_sum, ans = len(arr), 0, 0
    for i in range(k):
        cur_max_sum += arr[i]

    ans = cur_max_sum
    for i in range(k):
        cur_max_sum = cur_max_sum + arr[n - i - 1] - arr[k - i - 1]
        ans = max(ans, cur_max_sum)
    return ans


print(pick_from_both_sides([5, -2, 3, 1, 2], 3))
print(pick_from_both_sides([2, 3, -1, 4, 2, 1], 4))
