"""
    Given an array, arr[] of size N, the task is to find the count of array indices such that removing an element from these indices makes the sum of even-indexed and odd-indexed array elements equal.
"""


def special_index(arr):
    even_sum, odd_sum, n = 0, 0, len(arr)
    even_prefix, odd_prefix = [], []
    left_sum, right_sum, count = 0, 0, 0

    for i in range(n):
        if i & 1 == 0:
            even_sum += arr[i]
            even_prefix.append(even_sum)
            odd_prefix.append(odd_sum)
        else:
            odd_sum += arr[i]
            even_prefix.append(even_sum)
            odd_prefix.append(odd_sum)

    for i in range(n):
        if i == 0:
            left_sum = even_prefix[n - 1] - even_prefix[i]
            right_sum = odd_prefix[n - 1] - odd_prefix[i]
        else:
            left_sum = even_prefix[i - 1] + odd_prefix[n - 1] - odd_prefix[i]
            right_sum = odd_prefix[i - 1] + even_prefix[n - 1] - even_prefix[i]

        if left_sum == right_sum:
            count += 1

    return count


print(special_index([2, 1, 6, 4]))
print(special_index([1, 1, 1]))
