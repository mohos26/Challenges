# https://edabit.com/challenge/cvxXvwRnEpekYbzzP
# 07.07.2025
# Hard

from math import sqrt, log10


def divisors(n):
    result = set()
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            result.add(i)
            result.add(n // i)
    return sorted(result)


def is_brilliant(n):
    lst = divisors(n)[1:-1]
    if len(lst) == 1 or (len(lst) == 2 and int(log10(lst[0])) == int(log10(lst[1]))):
        return True
    return False
