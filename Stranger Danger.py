# https://edabit.com/challenge/82AvsFFQprj43XCDS
# 6.11.2023
# Very Hard


def no_strangers(txt):
    d, result = dict(), [[], []]
    for i in txt.split():
        char = i.lower()
        while True:
            if not char[0].isalnum():
                char = char[1:]
            elif not char[-1].isalnum():
                char = char[:-1]
            else:
                break
        if char in list(d.keys()):
            d[char] += 1
            if d[char] == 5:
                result[1].append(char)
                result[0].remove(char)
            elif d[char] == 3:
                result[0].append(char)
        else:
            d.update({char: 1})
    return result
