# https://edabit.com/challenge/QoavwQhmrDpXJhBW9
# Medium
# 1.09.2023


def flip_list(lst):
    result = []
    if lst and type(lst[0]) == list:
        for i in lst:
            result.append(i[0])
        return result
    for i in lst:
        result.append([i])
    return result

def flip_list2(lst):
    if lst and type(lst[0]) == list:
        return list(map(lambda i: i[0], lst))
    return list(map(lambda i: [i], lst))
