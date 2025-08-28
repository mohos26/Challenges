# https://edabit.com/challenge/AdJNWPbfL9LunsNh9
# 18.07.2025
# Hard


def multiplication_table(n):
    lst = list(range(1, n + 1))
    res = []
    for i in range(1, n + 1):
        res.append(list(map(lambda x: x * i, lst)))
    return res
