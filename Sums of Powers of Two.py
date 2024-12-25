# https://edabit.com/challenge/yyCGJKP442qtTD9Ek
# 06.11.2024
# Very Hard


def sums_of_powers_of_two(n):
    res, aid, aid2 = [], bin(n)[:1:-1], 0
    for _ in range(aid.count('1')):
        aid2 += aid[aid2:].index('1')
        res.append(2**aid2)
        aid2 += 1
    return res

