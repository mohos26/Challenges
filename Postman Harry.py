# https://edabit.com/challenge/7yo5FJX4xFbNxim5q
# Very Hard
# 09.09.2024


def harry(lst):
    if lst == [[]]:
        return -1
    res = 0
    ind = 0
    for i in lst[:-1]:
        var = i[ind]
        for j in i[ind+1:]:
            if j == var:
                res += var
                ind += 1
            else:
                break
        res += var
    res += sum(lst[-1])
    return res
