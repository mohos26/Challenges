# https://edabit.com/challenge/hmt2HMc4XNYrwPkDh
# Hard
# 18.08.2024


def aid(s):
    # This function can be abbreviated by returning this expression:
    # chr(ord(s) + (-1*s.islower() +1*s.isupper())*32)
    if s.islower():
        return chr(ord(s) - 32)
    elif s.isupper():
        return chr(ord(s) + 32)
    return s

def invert(s):
    if len(s) == 1:
        return aid(s)
    return aid(s[-1]) + invert(s[:-1])

