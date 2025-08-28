# https://edabit.com/challenge/x3niK6ccbeQ5cC5kC
# hard


def elapsed(t1, t2):
    time, res = abs(t1-t2), []
    for i, lst in enumerate((('day', 86400), ('hour', 3600), ('minute', 60), ('second', 1))):
        aid = time//lst[1]
        if aid:
            res.append(str(aid) + ' ' + lst[0] + (aid > 1)*'s')
        time %= lst[1]
    return ', '.join(res)

print(elapsed(1559813526, 1559899926))
print(elapsed(1559681004, 1559899926))
