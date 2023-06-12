"""
    Given an integer array A containing N distinct integers, you have to find all the leaders in array A. An element is a leader if it is strictly greater than all the elements to its right side.
    NOTE: The rightmost element is always a leader.
"""


def leaders_array(arr):
    n = len(arr)
    cur_leader = arr[n - 1]
    result = [cur_leader]
    for i in range(n-2, -1, -1):
        if arr[i] > cur_leader:
            cur_leader = arr[i]
            result.append(cur_leader)
    return result


print(leaders_array([16, 17, 4, 3, 5, 2]))
print(leaders_array([5, 4]))
