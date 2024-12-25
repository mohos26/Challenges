# https://edabit.com/challenge/rMwssAueJjn9FmjZC
# 15.06.2024
# Hard


def number_pairs(txt):
    lst = list(map(int, txt.split()[1:]))
    i = result = 0
    while i != len(lst):
        if lst[i] in lst[i+1:]:
            result += 1
            lst[i+1:].remove(lst[i])
            lst.pop(i)
        i += 1
    return result


def number_pairs2(txt):
    lst = list(map(int, txt.split()))
    Len = lst[0]
    lst.pop(0)
    i = result = 0
    while Len:
        if lst[i] in lst[i+1:]:
            result += 1
            lst[i+1:].remove(lst[i])
            lst.pop(i)
            Len -= 1
        i += 1
        Len -= 1
    return result


def number_pairs_gpt(numbers_str):
    numbers = list(map(int, numbers_str.split()[1:]))
    count_dict = {}
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    pair_count = 0
    for count in count_dict.values():
        pair_count += count // 2
    return pair_count
