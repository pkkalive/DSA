"""
    Shaggy has an array A consisting of N elements. We call a pair of distinct indices in that
    array a special if elements at those indices in the array are equal.
    Shaggy wants you to find a special pair such that the distance between that pair is minimum.
    Distance between two indices is defined as |i-j|. If there is no special pair in the array,
    then return -1.
"""

import sys


def shaggy_distances(nums):
    min_diff = sys.maxsize
    my_map = {}
    for i in range(len(nums)):
        if my_map.get(nums[i]) is not None:
            curr_diff = i - my_map.get(nums[i])
            min_diff = min(min_diff, curr_diff)
        my_map.update({nums[i]: i})

    if min_diff == sys.maxsize:
        return -1
    return min_diff


print(shaggy_distances([7, 1, 3, 4, 1, 7]))
print(shaggy_distances([1, 1]))
