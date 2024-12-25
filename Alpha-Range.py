# https://edabit.com/challenge/rihSbQq6x8R2D4aoa
# 06.11.2024
# Very Hard


from string import ascii_uppercase as upper, ascii_lowercase as lower


def alpha_range(start, stop, step=1):
    res = []
    if not 0 < abs(step) < 26:
        res = 'step must be a non-zero value between -26 and 26, exclusive'
    elif (start+stop).isupper() or (start+stop).islower():
        caseType = [upper, lower][start.islower()]
        start = caseType.index(start)
        stop = caseType.index(stop)
        start, stop = min(start, stop), max(start, stop)
        if step < 0:
            start, stop = stop, start
        for i in range(start, stop+(1 -2*(step < 0)), step):
            res.append(caseType[i])
    else:
        res = 'both start and stop must share the same case'
    return res

