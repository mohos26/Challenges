# https://edabit.com/challenge/Sws7TmBqGJZfReepJ
# Very Hard
# 13.08.2024


def make_anagram(a, b):
    result = 0
    lst = [list(a), list(b)]
    for i in lst[0]:
        if i in lst[1]:
            lst[1].pop(lst[1].index(i))
            result += 1
    return len(a + b) - 2 * result

