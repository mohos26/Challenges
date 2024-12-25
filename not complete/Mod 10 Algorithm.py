# https://edabit.com/challenge/XKEDTh2NMtTLSyCc2
# 23.03.2024
# Very Hard


def valid_credit_card(number):
    lst = map(int, list(str(number))[::2])
    lst = map(lambda x: x*2, lst)
    var = sum(map(int, list(str(number))[1::2]))
    for i in lst:
        if i > 9:
            v = list(str(i))
            v = map(int, v)
            var += sum(v)
        else:
            var += i
    return var % 10 == 0


def valid_credit_card_gpt(number):
    num_str = str(number)
    num_str = num_str[::-1]
    doubled_digits = []
    for i in range(len(num_str)):
        digit = int(num_str[i])
        if i % 2 == 1:
            digit *= 2
        doubled_digits.append(digit)
    subtracted_digits = []
    for num in doubled_digits:
        if num > 9:
            subtracted_digits.append(num - 9)
        else:
            subtracted_digits.append(num)
    total = 0
    for num in subtracted_digits:
        total += num
    return total % 10 == 0
