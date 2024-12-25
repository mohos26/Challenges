# https://edabit.com/challenge/64w3Mpumi7kTA82Sv
# 19.07.2023
# Hard


def simple_symbols(txt):
    for i in range(len(txt)):
        if txt[i].isalpha() and ([0, len(txt)-1].count(i) or txt[i-1]+txt[i+1] != '++'):
            return False
    return True

def simple_symbols_gpt(txt):
    if txt[0].isalpha() or txt[-1].isalpha():
        return False
    for i in range(1, len(txt) - 1):
        if txt[i].isalpha():
            if txt[i - 1] != '+' or txt[i + 1] != '+':
                return False
    return True
