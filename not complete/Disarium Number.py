# https://edabit.com/challenge/yvJbdkmKHvCNtcZy9
# Hard
# 11.09.2024


from math import log10, floor

def is_disarium(n):
    temp = n
    res = 0
    base = floor(log10(n)) + 1
    for i in range(base, 0, -1):
        res += (n%10)**i
        n //= 10
    return res
