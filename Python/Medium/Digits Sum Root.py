# https://edabit.com/challenge/veCWQHJNgeZQCNbdY
# Meduim
# 13.08.2024

def root_digit(n):
    if n < 10:
        return n
    return root_digit(sum(map(int, list(str(n)))))
