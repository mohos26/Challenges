# https://edabit.com/challenge/MYZu2j5zKndMB2zdg
# Meduim
# 11.09.2024


def absolute(txt):
    txt = txt.lower().split()
    for _ in range(txt.count('a')):
        txt[txt.index('a')] = 'an absolute'
    return ' '.join(txt).capitalize()

