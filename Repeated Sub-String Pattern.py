# https://edabit.com/challenge/L2nw2N2YqZCboiaYM
# Very Hard
# 13.08.2024

from math import sqrt, ceil, floor

def common_divisor(n):
    if n == 1:
        return []
    lst = [1]
    var = sqrt(n)
    for i in range(2, ceil(var)):
        if n%i == 0:
            lst.append(i)
            lst.append(n//i)
    if floor(var) == var:
        lst.append(int(var))
    return lst

def Split(s, n):
    lst = []
    Len = len(s)
    for i in range(Len // n):
        lst.append(s[i*n:n*(i+1)])
    return lst

def is_repeated(lst):
    for i in lst[1:]:
        if lst[0] != i:
            return False
    return True

def repeated(s):
    Len = len(s)
    lst = common_divisor(Len)
    if lst:
        for i in lst:
            var = Split(s, i)
            if is_repeated(var):
                return True
    return False

