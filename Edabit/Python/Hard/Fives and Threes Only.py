# https://edabit.com/challenge/5ZDz5nDDPdfg5BH8K
# 07.10.2024
# Very Hard


def only_5_and_3(n):
    power, aid = 0, n
    while aid > 4:
        if not aid%5:
            return True
        aid = n - (3**power) * bool(power)
        power += 1
    return False

