# https://edabit.com/challenge/tnjY9dCGCQxtgJgau
# 29.06.2025
# Expert

from math import isqrt


def triple(n):
    m, a, b, c = 2, 3, 4, 5
    for _ in range(n-1):
        m = b + c
        a = (m - 1) + isqrt(2 * m * (m - 1))
        b = a + 1
        c = isqrt((a**2 + b**2))
    return a, b, c
