"""
    You are given an array A of integers of size N.
    Your task is to find the equilibrium index of the given array
    The equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.
    If there are no elements that are at lower indexes or at higher indexes, then the corresponding sum of elements is considered as 0.

    Note:
        Array indexing starts from 0.
        If there is no equilibrium index then return -1.
        If there are more than one equilibrium indexes then return the minimum index.
"""


def equilibrium_index(arr):
    prefix, cur_sum = [], 0
    n = len(arr)
    for num in arr:
        cur_sum += num
        prefix.append(cur_sum)

    for i in range(n):
        left_sum, right_sum = 0, 0
        if i == 0:
            right_sum = prefix[n - 1] - prefix[i]
        else:
            left_sum = prefix[i - 1]
            right_sum = prefix[n - 1] - prefix[i]

        if left_sum == right_sum:
            return i
    return -1


print(equilibrium_index([-7, 1, 5, 2, -4, 3, 0]))
print(equilibrium_index([1, 2, 3]))
