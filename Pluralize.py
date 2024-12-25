# https://edabit.com/challenge/LR98GCwLGYPSv8Afb
# 25.06.2023
# Hard


def pluralize(lst):
    lst2 = list(set(lst))
    Set = set()
    for i in lst2:
        if lst.count(i) > 1:
            Set.add(i + 's')
        else:
            Set.add(i)
    return Set
