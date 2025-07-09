# https://edabit.com/challenge/otJN6Bt4qR7kN4Jxt
# 07.07.2025
# Very Hard


def incremental_depth(lst):
    if len(lst) == 1:
        return lst
    return [lst[0], incremental_depth(lst[1:])]
