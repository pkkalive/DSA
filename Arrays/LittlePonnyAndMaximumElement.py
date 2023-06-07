"""
    Little Ponny is given an array, A, of N integers. In a particular operation, he can set any element of the array equal to -1.
    He wants your help in finding out the minimum number of operations required such that the maximum element of the resulting array is B. If it is not possible, then return -1.
"""


def ponny_maximum(arr, key):
    count, flag = 0, False
    for num in arr:
        if num == key:
            flag = True
        if num > key:
            count += 1

    if flag:
        return count
    return -1


print(ponny_maximum([2, 4, 3, 1, 5], 3))
print(ponny_maximum([1, 4, 2], 3))