# https://edabit.com/challenge/FiPf9yTEfo5aBikPF
# 24.04.2025
# Very Hard


def coins_combinations(money, coins):
	lst = [0] * (money + 1)
	lst[0] = 1
	for coin in coins:
		for i in range(coin, money + 1):
			lst[i] = lst[i - coin]
	return lst[money]
