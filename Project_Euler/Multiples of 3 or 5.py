# https://projecteuler.net/problem=1
# 28.08.2025


res = 0
for n in range(1, 1000):
	if not n % 3 or not n % 5:
		res += n

print(res)