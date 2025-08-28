# https://edabit.com/challenge/5ou6SKDtFRZugbpda
# 15.05.2025
# Hard


def additive_persistence(n):
	res = 0
	while n > 9:
		n = sum(map(int, str(n)))
		res += 1
	return res

def multiplicative_persistence(n):
	res = 0
	while n > 9:
		lst = map(int, str(n))
		n = 1
		for i in lst:
			n *= i
		res += 1
	return res

print(additive_persistence(27))
