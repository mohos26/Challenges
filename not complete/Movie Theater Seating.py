# https://edabit.com/challenge/dKeLAqAxpddbkvNhh
# 02.02.2023
# Very Hard

from math import ceil


def group_seats(lst, n):
    for i in range(len(lst)):
        nn = 0
        lst2 = []
        for j in lst[i]:
            if j == 0:
                nn += 1
            else:
                lst2.append(nn)
                nn = 0
        else:
            lst2.append(nn)
        for j in lst2:
            if j >= n:
                return i+1
    return 0

def group_seats2(lst, n):
    for i in range(len(lst)):
        if ''.join(list(map(lambda item: str(item), lst[i]))).count('0' * n):
            return i + 1
    return 0

def group_seats3(lst, n):
    return ceil((','.join(list(map(lambda l: ''.join(list(map(lambda item: str(item), l))), lst))).find('0'*n) + 1) / 8)
