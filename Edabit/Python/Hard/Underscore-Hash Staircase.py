# https://edabit.com/challenge/YqLBEZJR9ySndYQpH
# 26.10.2024
# Very Hard


def staircase(n):
    res = []
    for i in range(abs(n)):
        if n > 0:
            res.append((n-i-1)*'_' + (i+1)*'#')
        else:
            res.append((i)*'_' + (-n-i)*'#')
    return '\n'.join(res)

