# https://edabit.com/challenge/xCFHFha5sBmzsNARH
# Easy
# 06.08.2024


def reverse(txt):
    Len = len(txt)
    if not Len:
        return ''
    return txt[Len - 1] + reverse(txt[:Len - 1])

