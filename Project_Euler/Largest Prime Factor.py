# https://projecteuler.net/problem=4
# 28.08.2025

from math import sqrt

def next_prime(n):
	aid = True
	while aid:
		n += 1
		aid = True
		for i in range(2, int(sqrt(n))+1):
			if not n % i:
				break
		else:
			aid = False
	return n


prime = 2
n = 600851475143
while n - 1:
	if n % prime:
		prime = next_prime(prime)
	else:
		n /= prime

print(prime)
