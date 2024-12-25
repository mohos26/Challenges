# https://edabit.com/challenge/ZsLDkJfLGFkmjS2jE
# Medium
# 20.11.203


def diving_minigame(lst):
    var = 5
    for i in lst:
        if i < 0:
            var -= 1
        else:
            if (var + 2) / 5 <= 1:
                var += 2
            else:
                var = 5
        if var == 0:
            return False
    return True
