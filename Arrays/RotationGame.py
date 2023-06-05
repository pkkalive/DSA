"""
    Given an integer array A of size N and an integer B, you have to print the same array after
    rotating it B times towards the right.
"""


def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def rotation_game(nums, B):
    n = len(nums)
    k = B % n
    if k > 0:
        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)

    return nums


print(rotation_game([1, 2, 3, 4], 2))
