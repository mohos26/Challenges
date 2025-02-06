# https://edabit.com/challenge/ehyZvt6AJF4rKFfXT
# 08.11.2024
# Hard


def uncensor(txt, vowels):
    lst = list(txt)
    for letter in vowels:
        lst[lst.index('*')] = letter
    return ''.join(lst)

