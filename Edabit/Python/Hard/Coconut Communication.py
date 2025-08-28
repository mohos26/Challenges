# https://edabit.com/challenge/Kk5Ku4CtipaFtATPT
# 04.07.2025
# Very Hard


def coconut_translator(txt):
    res = []
    for c in map(ord, txt):
        res.append("")
        for a, b in zip("coconuts", bin(c)[2:].zfill(8)):
            if int(b):
                res[-1] += a.upper()
            else:
                res[-1] += a
    return " ".join(res)
