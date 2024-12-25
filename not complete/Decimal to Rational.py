# https://edabit.com/challenge/uGCJekBQnEq2Sui72

def ist(x, y):
    lst = [0]
    for i in range(1, min(x, y)+1):
        if not x%i and not y%i:
            lst.append(i)
    aid = max(lst)
    if not aid:
        return [0, 1]
    return [x//aid, y//aid]

def find_fraction(str_num):
    lst = [0, 1]
    aid2 = str_num.index('.')
    aid5 = str_num[aid2+1:]
    if '(' in str_num:
        aid4 = str_num[str_num.index('(')+1:str_num.index(')')]
        lst[0] += int(aid4)
        lst[1] *= 10**len(aid4)-1
        str_num = str_num[:str_num.index('(')]
        aid5 = aid5[:aid5.index('(')]
    aid3 = int(str_num[:aid2])
    if aid5:
        lst[0] += int(aid5)*lst[1]
        lst[1] *= 10**len(aid5)
    while True:
        aid = ist(*lst)
        if aid == lst:
            break
        lst = list(aid)
    lst[0] += aid3*lst[1]
    return tuple(lst)
