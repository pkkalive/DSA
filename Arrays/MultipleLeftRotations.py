"""
    Given an array of integers A and multiple values in B, which represents the number of times array A needs to be left rotated.
    Find the rotated array for each value and return the result in the form of a matrix where ith row represents the rotated array for the ith value in B.
"""


def multiple_left_rotations(arr, key):
    n = len(arr)
    k = key % n
    res = []
    for i in range(k, n):
        res.append(arr[i])
    for i in range(k):
        res.append(arr[i])
    return res


print(multiple_left_rotations([1, 2, 3, 4, 5], 2))  # [3, 4, 5, 1, 2]
print(multiple_left_rotations([1, 2, 3, 4, 5], 3))  # [4, 5, 1, 2, 3]
print(multiple_left_rotations([1, 2, 3, 4, 5], 5))
