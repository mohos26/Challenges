# https://edabit.com/challenge/4xZFisQX8NnYB3nv4
# Very Hard
# 06.08.2024


def check_places(main, lst, Len):
    lst2 = []
    for i in lst:
        if i >= 0 and i < Len:
            lst2.append(main[i])
    return not sum(lst2)

def maximum_seating(lst):
    result = 0
    Len = len(lst)
    for i in range(Len):
        if not lst[i] and check_places(lst, [i-2, i-1, i+1, i+2], Len):
            result += 1
            lst[i] = 1
    return result

