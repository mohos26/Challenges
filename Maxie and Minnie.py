# https://edabit.com/challenge/HqpZQPZiHbPK4HgEB
# Expect
# 12.08.2024


def swap(n, i, j):
    temp = n[i]
    n = n[:i] + n[j] + n[i+1:]
    n = n[:j] + temp + n[j+1:]
    return n

def maxmin(n):
    result = [n]
    n = str(n)
    for i in range(len(n) - 1):
        for j in range(i + 1, len(n)):
            var = swap(n, i, j)
            if var[0] != '0':
                result.append(int(var))
    return max(result), min(result)

