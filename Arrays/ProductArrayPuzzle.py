"""
    Given an array of integers A, find and return the product array of the same size where the ith element of the product array will be equal to the product of all the elements divided by the ith
    element of the array.
    Note: It is always possible to form the product array with integer (32 bit) values. Solve it without using the division operator.
"""


def product_array(arr):
    n = len(arr)
    product, prefix, suffix, ans = 1, [], [0]*n, [0]*n
    for num in arr:
        product *= num
        prefix.append(product)

    product = 1
    for i in range(n - 1, -1, -1):
        product *= arr[i]
        suffix[i] = product

    for i in range(n):
        if i == 0:
            ans[i] = suffix[i + 1]
        elif i == n - 1:
            ans[i] = prefix[i - 1]
        else:
            ans[i] = prefix[i - 1] * suffix[i + 1]
    return ans


print(product_array([5, 1, 10, 1]))
print(product_array([1, 2, 3, 4, 5]))
