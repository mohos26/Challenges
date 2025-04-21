# https://edabit.com/challenge/HwwspgCBsYQhMcafw
# Hard
# 18.08.2024


def aid(n):
    if n < 10:
        return n
    return n%10 + aid(n//10)

def super_digit(n, k):
    if len(n) == 1:
        return int(n)
    # str(sum(map(int, list(n*k))))
    return super_digit(str(aid(int(n*k))), 1)

