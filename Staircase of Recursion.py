# https://edabit.com/challenge/9S8qp4XKG2qwQMdrb
# Hard
# 21.08.2024


def ways_to_climb(n):
    if n < 2:
        return 1
    return ways_to_climb(n-1) + ways_to_climb(n-2)

