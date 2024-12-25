# https://edabit.com/challenge/6rztMMwkt6ijzqcF6
# 11.03.2023
# Medium


def is_repeated(strn):
    for i in range(1, len(strn)):
        if strn[:i] == strn[i: 2*i]:
            return strn.count(strn[:i])
    return False
