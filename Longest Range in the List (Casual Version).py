# https://edabit.com/challenge/9v34qtFufkqPmzeDu
# 09.06.24
# Hard


def max_consec(lst):
    lst = sorted(list(set(lst)))
    next_value = lst[0] + 1
    current_total = result = 1
    for i in lst:
        if next_value == i:
            current_total += 1
            next_value += 1
        else:
            next_value = i+1
            if current_total > result:
                result = current_total
            current_total = 1
    else:
        if current_total > result:
            result = current_total
    return result
