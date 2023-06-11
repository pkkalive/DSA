"""
    Given an array A of N integers.
    Count the number of elements that have at least 1 element greater than itself.
"""


def count_elements(arr):
    count, cur_max = 0, arr[0]
    for num in arr:
        if num > cur_max:
            cur_max = num
            count = 1
        if num == cur_max:
            count += 1
    return len(arr) - count


print(count_elements([3, 1, 2]))
print(count_elements([5, 5, 3]))
print(count_elements([7, 4, 2, 10, 5]))
