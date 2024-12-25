# https://edabit.com/challenge/HhSS3YReRhBxZAnzk
# 03.08.2023
# Medium


def gen_values(n, i):
    result, var = [], 0
    while var <= n:
        result.append(round(var, 2))
        var += i
    return result
