# https://edabit.com/challenge/YsD3af7LgaH6JRSCH
# 03.11.2024
# Very Hard


def time_adjust(now, hrs, mins, sec):
    lst = list(map(int, now.split(':')))
    for i, n in enumerate((hrs, mins, sec)):
        lst[i] += n
    for i in range(2, 0, -1):
        temp = lst[i]
        lst[i] = str(lst[i]%60).zfill(2)
        lst[i-1] += temp//60
    lst[0] = str(lst[0]%24).zfill(2)
    return ':'.join(lst)

