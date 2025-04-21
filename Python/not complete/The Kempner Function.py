# https://edabit.com/challenge/qQnWXBsQaH73yY8r4
# Hard

def kempner(n):
    if n < 2:
        return 1;
    return (n * kempner(n-1)) % 10
