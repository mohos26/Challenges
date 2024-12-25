# https://edabit.com/challenge/yYE8bJ5jhJgAoc5ir
# Meduim
# 10.08.2024

def bugger(num):
    if num < 10:
        return 0;
    return 1 + bugger((eval('*'.join(list(str(num))))))
