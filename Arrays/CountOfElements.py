"""
    Given an array A of N integers.
    Count the number of elements that have at least 1 element greater than itself.
"""


def count_elements(arr):
    count, cur_max = 1, arr[0]
    for i in range(1, len(arr)):
        if arr[i] > cur_max:
            cur_max = arr[i]
            count = 1
        elif arr[i] == cur_max:
            count += 1
    return len(arr) - count


print(count_elements([3, 1, 2]))
print(count_elements([5, 5, 3]))
print(count_elements([7, 4, 2, 10, 5]))
