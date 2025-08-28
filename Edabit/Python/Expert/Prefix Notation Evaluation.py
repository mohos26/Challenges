# https://edabit.com/challenge/uE5YuLZvpJu9TRnax
# 01.07.2025
# Expert

def ft_is_operation(s):
    for i in s:
        if i.isdigit():
            return False
    return True


def prefix(exp):
    j = 0
    lst = exp.split()
    for i in range(len(lst)):
        if ft_is_operation(lst[i]):
            j = i
    op, n1, n2 = lst[j:j+3]
    lst = lst[:j] + [str(int(eval(n1 + op + n2)))] + lst[j+3:]
    if len(lst) == 1:
        return int(lst[0])
    return prefix(" ".join(lst))
