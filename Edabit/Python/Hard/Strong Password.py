# https://edabit.com/challenge/QNvtMEBzxz5DvyXTe
# Very Hard
# 07.08.2024

def strong_password(password):
    result = 4;
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    lst = [numbers, lower_case, upper_case, special_characters]
    var = 6 - len(password)
    for i in password:
        for j in lst:
            if i in j:
                result -= 1
                lst.remove(j)
                break
    return max(result, var)

