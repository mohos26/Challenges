# https://edabit.com/challenge/rQkriLJBc9CbfRbJb
# 01.04.2023
# Easy


def index_of_caps(word):
    result = []
    for i, letter in enumerate(word):
        if letter.isupper():
            result.append(i)
    return result
