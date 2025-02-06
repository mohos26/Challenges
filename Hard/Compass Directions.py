# https://edabit.com/challenge/6LAgr6EGHKoZWGhjd
# 08.04.2024
# Hard


def final_direction(initial, turns):
    main = 'N', 'E', 'S', 'W'
    arg = main.index(initial) + sum(list(map(lambda x: (-1, 1)[x == 'R'], turns)))
    return main[arg % 4]
