# https://edabit.com/challenge/JAdCy7nMK8urjv9rL
# 14.06.2024
# Hard


from math import prod


def can_partition(lst):
    for i in range(len(lst)):
        if prod(lst[:i] + lst[i+1:]) in lst:
            return True
    return False


def can_partition2(lst):
    for i in (max(lst), min(lst)):
        ind = lst.index(i)
        if prod(lst[:ind] + lst[ind+1:]) in lst:
            return True
    return False


def can_partition_gpt(lst):
    total_product = 1
    for num in lst:
        total_product *= num
    for num in lst:
        if num != 0 and total_product % num == 0 and total_product // num == num:
            return True
    return False
