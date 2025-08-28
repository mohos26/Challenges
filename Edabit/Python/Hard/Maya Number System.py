#
#
#

d = {
    0: "@",
    1: "o",
    2: "oo",
    3: "ooo",
    4: "oooo",
    5: "-",
    6: "o-",
    7: "oo-",
    8: "ooo-",
    9: "oooo-",
    10: "--",
    11: "o--",
    12: "oo--",
    13: "ooo--",
    14: "oooo--",
    15: "---",
    16: "o---",
    17: "oo---",
    18: "ooo---",
    19: "oooo---",
}


def maya_number(n):
    res = []
    while n:
        res = [d[n % 20]] + res
        n //= 20
    if not res:
        return [d[0]]
    return res

print(maya_number(39))
