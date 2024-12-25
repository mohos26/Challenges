from itertools import combinations_with_replacement


def coins_combinations(money, coins):
    res = 0
    for i in range(1, money//min(coins)+1):
        for j in combinations_with_replacement(coins, i):
            if sum(j) == money:
                #print(list(j))
                res += 1
    return res

print(coins_combinations(11, [5,7]))
