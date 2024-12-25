# https://edabit.com/challenge/Azhkq898ZtmfyCGif
# 18.2.2023
# Very Hard


def numbers_to_ranges(lst):
    if not lst:
        return []

    ranges = last_i = lst[0]
    r = []
    for i in lst[1:]:
        if last_i + 1 != i:
            if ranges == last_i:
                r.append(f'{ranges}')
            else:
                r.append(f'{ranges}-{last_i}')
            ranges = i
        last_i = i
    else:
        if ranges == last_i:
            r.append(f'{ranges}')
        else:
            r.append(f'{ranges}-{last_i}')
    return r
