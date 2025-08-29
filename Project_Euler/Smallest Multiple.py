# https://projecteuler.net/problem=5
# 29.08.2025


N = 20
n = N
lst = range(N-1, 2, -1)
while True:
	for i in lst:
		if n % i:
			break
	else:
		break
	n += N

print(n)
