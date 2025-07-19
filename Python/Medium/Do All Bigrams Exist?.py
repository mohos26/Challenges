# https://edabit.com/challenge/7QPHWACcDihT3AM6b
# 04.11.2024
# Medium


def can_find(bigrams, words):
    aid = ' '.join(words)
    for iteam in bigrams:
        if not iteam in aid:
            return False
    return True

