# https://edabit.com/challenge/sw5LQa7meG4DGzaeg
# Meduim
# 03.09.2024


def multiply(lst):
    def aid(n):
        for i in range(len(lst)):
            lst[i] *= n
        return lst
    return aid
