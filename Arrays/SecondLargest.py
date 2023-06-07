"""
    You are given an integer array A. You have to find the second-largest element/value in the array or report that no such element exists.
"""


def second_largest(arr):
    largest, next_largest = -1, -1
    for num in arr:
        if num > largest:
            next_largest = largest
            largest = num
        if largest > num > next_largest:
            next_largest = num

    return next_largest


print(second_largest([2, 1, 2]))
print(second_largest([11,15,19]))
print(second_largest([13, 7, 16, 18, 14, 17, 18, 8, 10]))
