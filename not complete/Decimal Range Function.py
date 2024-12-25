# https://edabit.com/challenge/aQWPiDnfwdE7xnqDq
# Very Hard
# 05.09.2024


def drange(*args):
    result = []
    if len(args) > 2:
        start, end, step = args[:3]
    elif len(args) == 2:
        start, end, step = *args, 1
    else:
        start, end, stap = 0, *args, 1
    var = start
    while var < end:
        result.append(var)
        var += step
    return tuple(result)
