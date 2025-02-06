# https://edabit.com/challenge/cx2KeDmEZDyeFsSfT
# 06.10.2024
# Hard

from math import log10

def _sum(n):
    if not n:
        return 0
    return n%10 + _sum(n//10)


def periodic(n):
    lenght, aid, count, lst = len(n)-1, int(n), 0, []
    while aid not in lst:
        lst.append(aid)
        aid = (aid%10**lenght*10**int(log10(_sum(aid))+1) + _sum(aid))%10**(lenght+1)
        count += 1
    return count
