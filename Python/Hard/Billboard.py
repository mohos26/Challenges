# https://edabit.com/challenge/eDQDChGrv6y4fd44j
# 26.10.2024
# Very Hard


def can_put(txt, dim):
    lst = txt.split(maxsplit=dim[0]-1)
    if max(map(lambda s: len(s), lst)) > dim[1]:
        return False
    return True

