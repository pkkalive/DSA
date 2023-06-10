"""
    You are given an integer array A of length N.
    You are also given a 2D integer array B with dimensions M x 2, where each row denotes a [L, R] query.
    For each query, you have to find the sum of all elements from L to R indices in A (0 - indexed).
    More formally, find A[L] + A[L + 1] + A[L + 2] +... + A[R - 1] + A[R] for each query.
"""


def range_query_sum(arr, query):
    cur_sum, prefix_sum, ans = 0, [],  []
    for num in arr:
        cur_sum += num
        prefix_sum.append(cur_sum)

    for [left, right] in query:
        if left == 0:
            ans.append(prefix_sum[right])
        else:
            ans.append(prefix_sum[right] - prefix_sum[left - 1])
    return ans


print(range_query_sum([1, 2, 3, 4, 5], [[0, 3], [1, 2]]))
print(range_query_sum([2, 2, 2], [[0, 0], [1, 2]]))
