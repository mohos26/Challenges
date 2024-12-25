# https://edabit.com/challenge/oQGhFdj2HHnFEjtAx
# 08.10.2024
# Expect


def _cute(txt, i, reverse):
    if reverse:
        return txt[:i]
    return txt[i+1:]

def slicer(txt, slic):
    lst, cp_txt, aid, i, reverse = [], txt, 0, 0, False
    while i < len(slic):
        aid2 = cp_txt.find(slic[i])
        if aid2 == -1:
            lst, cp_txt, aid, i, reverse = [], txt, 0, 0, True
        else:
            lst.append(aid + aid2)
            if not reverse:
                aid += aid2+1
            cp_txt = _cute(cp_txt, aid2, reverse)
            i += 1
    if len(lst) == 1:
        return str(lst)
    step, start, end = lst[1]-lst[0], lst[0], lst[-1]+1
    if start == 0 or start+1 == len(txt):
        start = ''
    if step > 0:
        if end+step > len(txt):
            end = ''
        if step == 1:
            return f'[{start}:{end}]'
    else:
        end -= 2
        if end - abs(step) + 1 < 0:
            end = ''
    return f'[{start}:{end}:{step}]'

