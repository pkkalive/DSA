"""
    You are given a string S, and you have to find all the amazing substrings of S.
    An amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).
"""


def amazing_sub_arrays(string):
    my_map = {
        'a': True,
        'e': True,
        'i': True,
        'o': True,
        'u': True,
        'A': True,
        'E': True,
        'I': True,
        'O': True,
        'U': True,
    }
    mod, count, n = 10003, 0, len(string)
    for i in range(n):
        if my_map.get(string[i]) is not None:
            count = count + ((n - i) % mod)

    return count


print(amazing_sub_arrays("pGpEusuCSWEaPOJmamlFAnIBgAJGtcJaMPFTLfUfkQKXeymydQsdWCTyEFjFgbSmknAmKYFHopWceEyCSumTyAFwhrLqQXbWnXSn"))
