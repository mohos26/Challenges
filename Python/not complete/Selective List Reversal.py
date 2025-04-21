# https://edabit.com/challenge/35JtGyWLFhxGkHNnj
# Very hard
# 11.09.2023


def sel_reverse(lst, length):
    """lst1, var, result = [[]], 0, []
    for i in lst:
        lst1[-1].append(i)
        var += 1
        if var >= length:
            var = 0
            lst1.append([])
    for i in lst1:
        for j in sorted(i, reverse=True):
            result.append(j)
    return result"""
    sublists = sublist = []
    for i in lst:
        sublist.append(i)
        if len(sublist) == length:
            sublists.append(sublist[::-1])
            sublist = []
    if sublist:
        sublists.append(sublist[::-1])
    result = [elem for sublist in sublists for elem in sublist]
    return result

def sel_reverse_gpt(lst, n):
    if n <= 0:
        return lst
    elif n >= len(lst):
        return lst[::-1]
    else:
        reversed_list = []
        for i in range(0, len(lst), n):
            chunk = lst[i:i + n]
            reversed_list.extend(chunk[::-1])
        return reversed_list
