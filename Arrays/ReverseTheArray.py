"""
    You are given a constant array A.
    You are required to return another array which is the reversed form of the input array.
"""


def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left <= right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


print(reverse_array([1, 2, 3, 2, 1]))
print(reverse_array([1, 1, 10]))