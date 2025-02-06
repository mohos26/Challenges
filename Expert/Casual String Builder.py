# https://edabit.com/challenge/F9r7cuye3EbNRBtjx
# 23.09.2024
# Expect

from math import log10


def select_num(txt):
    res = ''
    for i in txt[::-1]:
        if i.isdigit():
            res += i
        else:
            break
    return int(res[::-1])


def faid(txt, start):
    aid = 0
    for i in range(start+1, len(txt)):
        if txt[i] == '[':
            aid += 1
        elif txt[i] == ']':
            if not aid:
                return i
            aid -= 1
    return False


def string_builder(txt):
    while txt.count('['):
        aid = 0
        start = txt.index('[')
        n = select_num(txt[:start])
        end = faid(txt, start)
        txt = txt[:start-int(log10(n))-1] + n * txt[start+1:end] + txt[end+1:]
    return txt
