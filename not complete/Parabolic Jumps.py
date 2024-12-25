# https://edabit.com/challenge/MFFuPFnjT8ihniKtL
# 22.03.2024
# Very Hard


def bug_jump(height, time):
    time = time/1000
    t = 2*(height**0.5)
    m = round(-(time**2) + t*time, 2)
    if m <= 0:
        return 0, None
    return m, ('up', 'down')[t/2 < time]


def bug_jump_gpt(height, time):
    g = 9.8 / 100
    t = time / 1000
    position = -0.5 * g * t**2 + height
    if position <= 0:
        return 0, None
    direction = "up" if position > 0 else "down"

    return [round(position, 2), direction]
