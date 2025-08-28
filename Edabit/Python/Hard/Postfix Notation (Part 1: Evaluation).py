# https://edabit.com/challenge/xWW8PMuLN8hmAgLMJ
# 27.10.2024
# Very Hard


def postfix(expression):
    lst = expression.split()
    while len(lst) != 1:
        for i, iteam in enumerate(lst):
            if iteam in ('+', '-', '/', '*'):
                lst = lst[:i-2] + [str(eval(lst[i-2] + lst[i] + lst[i-1]))] + lst[i+1:]
                break
    return round(float(lst[0]))

