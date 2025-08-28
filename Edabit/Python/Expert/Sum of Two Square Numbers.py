# https://edabit.com/challenge/y9q4ZbaThohALNqqJ
# Expect
# 14.08.2024


from math import sqrt

def squares_sum(n):
    a = int(sqrt(n))
    for i in range(a+1):
        b = int(sqrt(n - i**2))
        if (i**2 + b**2) == n:
            return True
    return False

