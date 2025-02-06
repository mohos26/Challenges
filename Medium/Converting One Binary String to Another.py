# https://edabit.com/challenge/AjZBGWyPaA7rXFhi6
# Meduim
# 14.08.2024


def min_swaps(s1, s2):
    if len(s1) == 1:
        return (s1[0] != s2[0]) * 0.5
    return (s1[0] != s2[0]) * 0.5 + min_swaps(s1[1:], s2[1:])


