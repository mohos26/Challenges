# https://edabit.com/challenge/7soAnzpZToSxztnDr
# Hard
# 18.08.2024


def shift_left(x, y):
    # You can sum up all this nonsense with this expression:
    # x * 2**y
    if y == 0:
        return x
    return x * 2 * shift_left(1, y-1)

