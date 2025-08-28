# https://edabit.com/challenge/YcqAY72nZNPtvofuJ
# 04.05.2025
# Very Hard


def quad_sequence(lst):
	res = [lst[-1]]
	arg = lst[-1] - lst[-2]
	aid = lst[2] - lst[1] * 2 + lst[0]
	for _ in range(len(lst)):
		arg += aid
		res.append(res[-1] + arg)
	return res[1:]
