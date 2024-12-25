# https://edabit.com/challenge/aifM22oGtRKShsFWB
# Hard
# 11.09.2024


from math import log10, floor

def disarium(n):
    if n == 0:
        return 0
    return (n%10)**floor(log10(n)+1) + disarium(n//10)

def is_disarium(n):
    return disarium(n) == n

