# https://edabit.com/challenge/k7YPvRyJt9NHbrvzu
# 12.07.2023
# Expect


from itertools import combinations_with_replacement


def football(score):
    lst = []
    for i in [2, 3, 6, 7, 8]:
        if i > score:
            break
        else:
            lst.append(str(i))

    result, lst2 = 0, []
    for i in range(1, score//2+1):
        lst2 += list(combinations_with_replacement(lst, i))
    for i in lst2:
        if sum(list(map(int, i))) == score:
            result += 1

    return result

def football_gpt(score):
    ways = [0] * (score + 1)
    ways[0] = 1  # There's one way to reach a score of 0 (no play)

    for i in range(2, score + 1):
        ways[i] += ways[i - 2]  # Add the ways to reach (i-2)
        if i >= 3:
            ways[i] += ways[i - 3]  # Add the ways to reach (i-3)
        if i >= 6:
            ways[i] += ways[i - 6]  # Add the ways to reach (i-6)
        if i >= 7:
            ways[i] += ways[i - 7]  # Add the ways to reach (i-7)
        if i >= 8:
            ways[i] += ways[i - 8]  # Add the ways to reach (i-8)

    return ways[score]

