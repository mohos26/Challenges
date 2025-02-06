# https://edabit.com/challenge/ZF9e922XuRaMu43Wp
# 28.10.2024
# Very Hard


def stair(steps):
    if steps == 0:
        return '___'
    res = ' '*steps*2 + '_\n'
    for i in range(steps-1, 0, -1):
        res += ' '*i*2 + '_|\n'
    res += '_|'
    return res

