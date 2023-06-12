"""
    You are given an integer array A.
    Decide whether it is possible to divide the array into one or more sub-arrays of even length such that the first and last element of all sub-arrays will be even.
    Return "YES" if it is possible; otherwise, return "NO" (without quotes).
"""


def even_sub_arrays(arr):
    n = len(arr)
    if n & 1 == 0 and arr[0] & 1 == 0 and arr[n - 1] & 1 == 0:
        return "YES"
    return "NO"


print(even_sub_arrays([2, 4, 8, 6]))
print(even_sub_arrays([2, 4, 8, 7, 6]))
print(even_sub_arrays(
    [654, 50, 694, 750, 712, 275, 736, 146, 279, 816, 707, 396, 406, 589, 370, 742, 840, 290, 505, 23, 249, 447, 618, 80, 968, 189, 600, 662, 91, 604, 575, 689, 72, 196, 475, 198, 850, 844, 361, 419, 617, 911, 268, 628,
     408, 404, 477, 921, 478, 806, 204, 637, 403, 911, 589, 529, 867, 584, 768, 257, 437, 380, 698, 452, 368, 97, 977, 582, 775, 103]))
