# https://edabit.com/challenge/si2H6WC5YX99cn6LQ
# Easy
# 04.08.2024

def sum_numbers(n):
    if  not n:
        return n
    return n + sum_numbers(n-1)
