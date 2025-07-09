# https://edabit.com/challenge/FJ8SmixDM6z3epzGy
# 09.07.2025
# Medium


from math import sqrt, ceil, floor


def multiples(n):
    lst, var = [], []
    var2 = sqrt(n)
    for i in range(1, ceil(var2)):
        if not n % i:
            lst.append(i)
            lst.append(n//i)
    if var2 == floor(var2):
        var = [floor(var2)]
    return lst[::2] + var + lst[::-2]


def check_perfect(num):
    return sum(multiples(num)[:-1]) == num
