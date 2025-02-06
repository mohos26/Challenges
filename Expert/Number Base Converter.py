# https://edabit.com/challenge/L2nw2N2YqZCboiaYM
# 02.11.2024
# Expect


def base_conv(n, b):
    if type(n) == int:
        lst = []
        while n:
            lst.append(n%b)
            n //= b
        return ''.join(map(lambda x: chr(x + 97), lst))[::-1]
    res = aid = 0
    for letter in n[::-1]:
        aid2 = ord(letter) -97
        if aid2 >= b or not letter.isalpha():
            return f'{n} is not a base {b} number.'
        res += b**aid * aid2
        aid += 1
    return res

