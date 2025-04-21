# https://edabit.com/challenge/yvJbdkmKHvCNtcZy9
# Hard
# 11.09.2024 -> 20.04.2025


def is_disarium(n):
	res = 0
	for i, d in enumerate(str(n)):
		res += int(d)**(i + 1)
	return res == n
