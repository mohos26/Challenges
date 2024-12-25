# https://edabit.com/challenge/EPXH424t2SSjMzms5
# 02.06.2024
# Medium


def remix(txt, lst):
    result = ['']*len(txt)
    for i, arg in enumerate(lst):
        result[arg] = txt[i]
    return ''.join(result)
