"""
    You are given an integer T (number of test cases). You are given array A and an integer B for each test case.
    You have to tell whether B is present in array A or not.
"""


def search_element(arr, key):
    for item in arr:
        if key == item:
            return 1

    return 0


print(search_element([4, 1, 5, 9, 1], 5))
print(search_element([7, 7, 2], 1))