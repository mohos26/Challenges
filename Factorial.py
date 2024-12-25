# https://edabit.com/challenge/x6McEkHer8A3Hke2q
# 23.2.2023
# Medium


from math import ceil, factorial

def factorial1(num):
    if num == 1:
        return 1
    return factorial(num-1)*num

def factorial2(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result

def factorial3(num):
    result = 1
    for i in range(1, num // 2 + 1):
        result *= i * (num-i+1)
    return result * (num % 2 * ceil(num / 2))

def factorial4(num):
    return factorial(num)
