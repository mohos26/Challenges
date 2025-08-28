from math import inf


def _aid(lst):
    aid  = inf
    if len(lst)%2:
        for i in range(len(lst)//2+1):
            if not aid > lst[i]:
                return False
            aid = lst[i]
        aid = -inf
        for i in range(len(lst)//2, len(lst)):
            if not aid < lst[i]:
                return False
            aid = lst[i]
    else:
        for i in range(len(lst)//2):
            if not aid > lst[i]:
                return False
            aid = lst[i]
        aid -= 1
        for i in range(len(lst)//2, len(lst)):
            if not aid < lst[i]:
                return False
            aid = lst[i]
    return True


def max_sum_pair(lst):
    res = []
    i = 0
    while i < len(lst):
        aid = []
        for j in range(i, len(lst)):
            aid.append(lst[i:j+1])
        aid2 = []
        for j in aid:
            if _aid(j):
                print(j)
                aid2.append(j)
        res.append(max(aid2, key=lambda l:len(l)))
        i += 1
    return res
