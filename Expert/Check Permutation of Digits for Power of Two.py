# https://edabit.com/challenge/RwCRpmhL7WTzpr6df
# 14.03.2023
# Expert


from math import log
from itertools import permutations


def check_power2(n):
    ls = list(map(lambda ls1: ''.join(ls1), list(permutations(list(str(n))))))
    ls2 = []
    for i in ls:
        ls2.append(int(log(int(i), 2).is_integer()))
    return bool(sum(ls2))


