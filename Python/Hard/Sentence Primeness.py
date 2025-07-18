# https://edabit.com/challenge/XKSwuu4ddzBvkXjvf
# 18.07.2025
# Very Hard

from math import sqrt, ceil, floor


def multiples(n):
    lst, var = [], []
    var2 = sqrt(n)
    for i in range(1, ceil(var2)):
        if not n % i:
            lst.append(i)
            lst.append(n // i)
    if var2 == floor(var2):
        var = [floor(var2)]
    return lst[::2] + var + lst[::-2]


def ft_aid(s):
    res = []
    lst = s.lower().split()
    for word in lst:
        res.append(0)
        for letter in word:
            if letter.isalpha():
                res[-1] += ord(letter) - 96
            else:
                res[-1] += int(letter)
    return res


def sentence_primeness(sentence):
    aid = ''
    for letter in sentence:
        if letter.isalnum() or letter == ' ':
            aid += letter
    lst = ft_aid(aid)
    if len(multiples(sum(lst))) == 2:
        return "Prime Sentence"
    for word, n in zip(aid.split(), lst):
        if len(multiples(sum(lst) - n)) == 2:
            return f"Almost Prime Sentence ({word})"
    return "Composite Sentence"
