"""
    You are given an integer array A of length N consisting of 0's & 1's, and an integer B.
    You have to tell all the indices of array A that can act as a center of 2 * B + 1 length 0-1 alternating subarray.
    A 0-1 alternating array is an array containing only 0's & 1's, and having no adjacent 0's or 1's. For e.g. arrays [0, 1, 0, 1], [1, 0] and [1] are 0-1 alternating, while [1, 1] and [0, 1, 0, 0, 1] are not.
"""


# TC : O(N)
def alternating_sub_array(arr, k):
    left, right, n = 0, 0, len(arr)
    ans = []
    size = 2 * k + 1
    if k == 0:
        for i in range(n):
            ans.append(i)
        return ans

    while right + 1 < n:
        if left == right:
            right += 1
            if arr[left] == arr[right]:
                left = right
        if right + 1 < n and arr[right] == arr[right + 1]:
            left = right + 1
            right += 1
        else:
            right += 1
            if right - left + 1 >= size and right < n:
                ans.append(right - k)
    return ans


print(alternating_sub_array([1, 0, 1, 0, 1], 1))
print(alternating_sub_array([0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1], 1))


# TC: O(N^2)
def alternating_sub_array_2(arr, k):
    n = len(arr)
    ans = []
    start = 0
    size = 2 * k + 1
    for i in range(n - size + 1):
        flag = arr[i]
        correct = True
        for j in range(i, i + size):
            if arr[j] == flag:
                flag = 1 - flag
            else:
                correct = False
        if correct:
            ans.append(i + size//2)
    return ans


print(alternating_sub_array_2([1, 0, 1, 0, 1], 1))
print(alternating_sub_array_2([0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1], 1))
