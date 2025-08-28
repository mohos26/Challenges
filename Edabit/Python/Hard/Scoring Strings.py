# https://edabit.com/challenge/zp64GNJQpZyGpYWL8
# 24.06.2025
# Very Hard


def score_it(s):
	i, n, res = 0, 0, 0
	for c in s:
		if c == '(':
			res += n * i
			i += 1
			n = 0
		elif c == ')':
			res += n * i
			i -= 1
			n = 0
		elif c.isdigit():
			n = n * 10 + int(c)
	return res
