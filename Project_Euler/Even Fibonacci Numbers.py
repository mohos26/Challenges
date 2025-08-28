# https://projecteuler.net/problem=3
# 28.08.2025


res, a, b = 0, 1, 1

while b < 4_000_000:
	a, b, = b, a + b
	if not b % 2:
		res += b

print(res)
