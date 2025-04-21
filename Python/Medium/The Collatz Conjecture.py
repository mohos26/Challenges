# https://edabit.com/challenge/X8fNb5EouWxrMMjZL
# Medium
# 07.08.2024

def collatz(num):
    if num == 1:
        return 0
    if not num % 2:
        return 1 + collatz(num // 2)
    return 1 + collatz(num * 3 + 1)

