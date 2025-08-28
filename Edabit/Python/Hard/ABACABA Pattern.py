# https://edabit.com/challenge/FDzEFbNE2q3eKL8dm
# Hard
# 19.08.2024


def abacaba_pattern(n):
    if n == 0:
        return ''
    return abacaba_pattern(n-1) + chr(n + 64) + abacaba_pattern(n-1)


