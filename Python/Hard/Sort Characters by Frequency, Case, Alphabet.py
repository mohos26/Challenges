# https://edabit.com/challenge/ik9CtowAndmAiStze
# Very Hard
# 09.08.2024

def ft_sort(main_lst, lst):
    Len = len(main_lst)
    i = 0
    while i < Len:
        j = i + 1
        while j < Len:
            if main_lst[i] < main_lst[j]:
                temp = main_lst[i]
                main_lst[i] = main_lst[j]
                main_lst[j] = temp
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
            j += 1
        i += 1
    return lst

def frequency_sort(s):
    lst = list(set(s))
    lst_count = []
    result = []
    for i in lst:
        var = s.count(i)
        if var not in lst_count:
            lst_count.append(var)
            result.append([])
        result[lst_count.index(var)].append(i)
    result = ft_sort(lst_count, result)
    for i in range(len(lst_count)):
        var = ''
        for j in sorted(result[i]):
            var += j * lst_count[i]
        result[i] = var
    return ''.join(result)

def frequency_sort2(s):
    lst = list(set(s))
    d = {}
    result = ''
    for i in lst:
        var = s.count(i)
        if var not in d.keys():
            d[var] = []
        d[var].append(i)
    for i in sorted(d.keys(), reverse=True):
        for j in sorted(d[i]):
            result += j * i
    return result

