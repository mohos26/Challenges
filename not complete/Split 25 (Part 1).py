# https://edabit.com/challenge/XjgoXNmnz59txiQp3
# 18.08.2023
# Very Hard


from itertools import combinations_with_replacement
from math import prod


def split(number):
    lst = []
    for i in range(1, number+1):
        lst += list(combinations_with_replacement(['1', '2', '3', '4', '5', '6', '7', '8', '9'], i))
    lst2 = []
    for i in lst:
        var = list(map(int, i))
        if sum(var) == number:
            lst2.append(prod(var))
    return sorted(lst2)[-1]

def split_gpt(n):
    if n <= 0:
        return 0
    max_products = [0] * (n + 1)
    max_products[1] = 1
    for i in range(2, n + 1):
        for j in range(1, i):
            max_products[i] = max(max_products[i], max(j, max_products[j]) * max(i - j, max_products[i - j]))
    return max_products[n]
