# https://edabit.com/challenge/v34oCTbkrceCZjgRE
# Meduim
# 08.08.2024


from math import floor
def shift_to_right(x, y):
    if y == 0:
        return x
    return floor(2**-1 * shift_to_right(x, y - 1))

