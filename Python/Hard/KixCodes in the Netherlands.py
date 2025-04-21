# https://edabit.com/challenge/XnByzPPcGo5CuTmZ4
# Very Hard
# 21.09.2023


from re import search


def kix_code(addr):
    l, v = addr.split(',')[2].split()[:2] + [addr.split(',')[1].split(maxsplit=1)[1]], ''
    l[-1] = l[-1][search(r"\d", l[-1]).start():]
    for i in l[-1]:
        if i.isalpha() or i.isalnum():
            v += i.upper()
        else:
            v += 'X'
    return ''.join(l[:2] + [v])
