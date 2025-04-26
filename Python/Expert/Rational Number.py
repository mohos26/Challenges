# https://edabit.com/challenge/8dkfsFEDNAbTqhAgc
# 26.04.2025
# Expert


def division(a, b):
	res = str(a // b) + '.'
	rem = a % b
	if not rem:
		return str(a / b)
	d = {}
	while rem > 0:
		if rem in d:
			res = res[:d[rem]] + "(" + str(res[d[rem]:]) + ")"
			break
		d.update({rem: len(res)})
		rem *= 10
		res += str(rem // b)
		rem %= b
	return res
