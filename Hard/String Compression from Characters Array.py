# link
# 02.10.2024
# Vey Hard


def _aid(letter, lenght):
    if lenght != 1:
        return letter + str(lenght)
    return letter

def compress(lst):
    letter, lenght, res = lst[0], 1, ''
    for i in range(1, len(lst)):
        if lst[i] == letter:
            lenght += 1
        else:
            res += _aid(letter, lenght)
            letter, lenght = lst[i], 1
    else:
        res += _aid(letter, lenght)
    return res

