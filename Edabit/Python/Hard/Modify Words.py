# https://edabit.com/challenge/ESAWnF3ySrFusHhYF
# 04.07.2025
# Hard


def edit_words(lst):
    res = []
    for arg in lst:
        aid = arg[:len(arg) // 2] + '-' + arg[len(arg) // 2:]
        res.append(aid.upper()[::-1])
    return res
