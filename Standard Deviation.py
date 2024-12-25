# https://edabit.com/challenge/frC4AdY2u4tm9aTRz
# 23.07.2023
# Medium


def standard_deviation(lst):
    result = 0
    for i in lst:
        result += (i - sum(lst) / len(lst))**2
    return round((result/len(lst))**(1/2), 2)
