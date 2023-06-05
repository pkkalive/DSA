"""
    Given an array A and an integer B. A pair(i, j) in the array is a good pair if i != j and
    (A[i] + A[j] == B). Check if any good pair exist or not.
"""


def good_pair(nums, key):
    my_dist = {}
    for num in nums:
        sum_to_be = key - num
        if my_dist.get(sum_to_be) is not None:
            return 1
        my_dist.update({num: True})

    return 0


print(good_pair([1, 2, 3, 4], 7))
print(good_pair([1, 2, 4], 4))
print(good_pair([1, 2, 2], 4))
