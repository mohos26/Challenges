# https://projecteuler.net/problem=4
# 28.08.2025


from math import sqrt, log10


def is_palindrome(n):
	original = n
	rev = 0
	while n:
		rev *= 10
		rev += n % 10
		n //= 10
	return original == rev


def ft_aid(n):
	for i in range(int(sqrt(n)), 1, -1):
		if not n % i:
			return i
	return 1


n = 999 * 999

while True:
	n -= 1
	if is_palindrome(n):
		a = ft_aid(n)
		b = n // a
		if int(log10(a)) == int(log10(b)) == 2:
			break

print(n)
