# https://edabit.com/challenge/5fjAbvQwW3akZDior
# 02.11.2024
# Medium

def unrepeated(txt):
    res = ''
    for letter in txt:
        if letter not in res:
            res += letter
    return res

