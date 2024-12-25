# https://edabit.com/challenge/Rep3fHbrLGKDatZ2L
# Expect
# 22.09.2024

from math import ceil

def _pattern(pat, lenght, ind=None):
    res = ''
    res += pat*(lenght//len(pat))
    res += pat[:lenght%len(pat)]
    if ind is not None:
        return res[:ind] + '_' + res[ind+1:]
    return res

def complete_pattern(txt):
    aid = txt.index('_')
    if aid < ceil(len(txt)/2)-len(txt)%2:
        main = txt[aid+1:]
    else:
        main = txt[:aid]
    i = 0
    while i < len(main)//2:
        if main[:i+1]*(len(main)//(i+1)) in main:
            if _pattern(main[:i+1], len(txt), aid) == txt:
                return _pattern(main[:i+1], len(txt))[aid]
            i = -1
            main = main[1:]
        i += 1
    i = ceil(len(main)/2)
    while i < len(main):
        if main[i:] in main[:i]:
            if _pattern(main[:i], len(txt), aid) == txt:
                return _pattern(main[:i], len(txt))[aid]
            i = -1
            main = main[1:]
        i += 1
    return _pattern(main, len(txt))[aid]
