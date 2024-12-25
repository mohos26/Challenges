# https://edabit.com/challenge/fbqmyDjCigbYhWLJa
# Expert
# 11.09.2024


def split_into_buckets(phrase, n):
    res = []
    words = phrase.split()
    for word in words:
        if res and len(res[-1]) + len(word) + 1 <= n:
            res[-1] += ' ' + word
        elif len(word) <= n :
            res.append(word)
        else:
            break
    return res

