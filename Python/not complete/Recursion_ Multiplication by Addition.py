# https://edabit.com/challenge/nimEZ6nfJ2vqzYBTL
# 21.03.2023
# Expect


n3 = 0
def multiply(n1, n2):
    global n3
    n3 += 1
    if n2 == 1:
        n3 = 0
        return n1
    return multiply(n1+(n1//n3), n2-1)

def multiply_gpt(x, y):
    if y == 0:
        return 0
    elif y > 0:
        return x + multiply(x, y-1)
    else:
        return -multiply(x, -y)
