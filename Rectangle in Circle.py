# https://edabit.com/challenge/cH3WN6TsqEC3qDg8f
# Meduim
# 07.08.2024


from math import sqrt


def rectangle_in_circle(w, h, radius):
    diameter = radius * 2
    diagonal = sqrt(w**2 + h**2)
    return diameter >= diagonal

