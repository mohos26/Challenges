# linkhttps://edabit.com/challenge/jWHkKc2pYmgobRL8R
# 08.10.2024
# Very Hard


def distance_to_nearest_vowel(txt):
    vowels, i, res = 'aeiou', 1, []
    for letter in txt:
        if letter in vowels:
            i = 0
        res.append(i)
        i += 1
    return res

