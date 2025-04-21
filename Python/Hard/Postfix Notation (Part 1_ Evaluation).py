# https://edabit.com/challenge/xWW8PMuLN8hmAgLMJ
# 25.07.2023
# Very Hard


def postfix(expression):
    expression = expression.split()
    while True:
        for i, arg in enumerate(expression):
            if not arg.isalnum():
                var = expression
                expression = list(expression[:i - 2]) + [str(int(eval(expression[i - 2] + arg + expression[i - 1])))]
                if len(var) > i + 1:
                    expression += var[i + 1:]
                break
        else:
            break
    return expression[0]

# 27.10.2024


def postfix(expression):
    lst = expression.split()
    while len(lst) != 1:
        for i, iteam in enumerate(lst):
            if iteam in ('+', '-', '/', '*'):
                lst = lst[:i-2] + [str(eval(lst[i-2] + lst[i] + lst[i-1]))] + lst[i+1:]
                break
    return round(float(lst[0]))

