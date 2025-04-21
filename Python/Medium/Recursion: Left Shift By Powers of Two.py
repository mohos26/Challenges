# https://edabit.com/challenge/g3BokS6KZgyYT8Hjm
# 06.11.2024
# Meduim


def shift_to_left(x, y):
    if not y:
        return x
    return 2*shift_to_left(x, y-1)

