# https://edabit.com/challenge/eoK63mG5tJDu439nJ
# 08.10.2024
# Expect


def _cmp(s1, s2):
    if len(s1) == len(s2):
        aid = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if aid:
                    return False
                aid += 1
        if aid:
            return True
    elif abs(len(s2) - len(s1)) == 1:
        if len(s1) > len(s2):
            lst = [s1, s2]
        else:
            lst = [s2, s1]
        for letter in lst[1]:
            if letter not in lst[0]:
                return False
            lst[0] = lst[0].replace(letter, '', 1)
        return True
    return False

def isWordChain(lst):
    aid = lst[0]
    for item in lst[1:]:
        if not _cmp(aid, item):
            return False
        aid = item
    return True

