# https://edabit.com/challenge/tMiJJkuAFDfsdmdZK
# 21.03.2023
# Medium


def to_snake_case(txt):
    lst = ['']
    for i in range(len(txt)):
        if txt[i].isupper():
            lst.append(txt[i].lower())
        else:
            lst[-1] += txt[i]
    return '_'.join(lst)

def to_camel_case(txt):
    txt = txt.split('_')
    for i in range(1, len(txt[1:])+1):
        txt[i] = txt[i].capitalize()
    return ''.join(txt)
