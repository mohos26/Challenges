# https://edabit.com/challenge/rBHTZ3HTCZQ6r5XP4
# Very Hard
# 11.09.2024


def expanded_form(num):
    res = []
    float_part = str(round(float(num) - int(num), 6))[2:]
    rm_zero = lambda lst: lst[1] != '0'
    for i, n in filter(rm_zero, list(enumerate(str(int(num))[::-1]))[::-1]):
        res.append(str(int(n)*10**i))
    if float_part != '0':
        for i, n in filter(rm_zero, enumerate(float_part)):
            res.append(n + '/' + str(10**(i+1)))
    return ' + '.join(res)

