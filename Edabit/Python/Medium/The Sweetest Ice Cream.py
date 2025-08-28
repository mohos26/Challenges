# https://edabit.com/challenge/uerTkWm9K3oMtMZKz
# Meduim
# 08.09.2024


def sweetest_icecream(lst):
    dct = {
    'Plain': 0,
    'Vanilla': 5,
    'ChocolateChip': 5,
    'Strawberry': 10,
    'Chocolate': 10
    }
    res = []
    for arg in lst:
        res.append(dct[arg.flavor] + arg.num_sprinkles)
    return max(res)

