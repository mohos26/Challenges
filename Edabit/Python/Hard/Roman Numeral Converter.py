# https://edabit.com/challenge/uPAmqwiHmvwpwoBom
# 2.05.2023
# Very hard


def convert_to_roman(num):
    lst = [
        ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
        ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
        ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
        ['', 'M', 'MM', 'MMM']]
    num = str(num)[::-1]
    result = []
    for i, n in enumerate(num):
        result.append(lst[i][int(n)])
    return ''.join(result[::-1])
