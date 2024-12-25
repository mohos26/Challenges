# https://edabit.com/challenge/437h8sNsWAPCcMRSg
# Very hard

from math import sqrt, ceil, floor


def aid(n):
    lst, var = [], []
    var2 = sqrt(n)
    for i in range(1, ceil(var2)):
        if not n%i:
            lst.append(i)
            lst.append(n//i)
    if var2 == floor(var2):
        var = [floor(var2)]
    return lst[::2] + var + lst[::-2]

def is_prime(lst):
    for n in lst:
        if len(aid(n)) != 2:
            return False
    return True

def product_of_primes(num):
    lst = aid(num)
    if floor(sqrt(num))**2 == num:
        return is_prime(sqrt(num))
    return len(lst) == 4 and is_prime(lst[1:-1])

