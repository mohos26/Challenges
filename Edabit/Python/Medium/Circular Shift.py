# https://edabit.com/challenge/nRAxMKDgcBTDeLzPz
# Medium
# 13.09.2023


def circular_shift(lst1, lst2, n):
    Len = len(lst1)
    result = [None] * Len
    for i, arg in enumerate(lst2):
        var = i+n
        while var >= Len or var < 0:
            if var >= Len:
                var -= Len
            else:
                var += Len
        result[var] = arg
    return result == lst1
