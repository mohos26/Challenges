# https://edabit.com/challenge/s45bQoPtMoZcj7rnR
# 24.06.2025
# Hard


def ft_aid(n):
	n = str(n)
	if len(n) == 1:
		return True
	return n[:len(n)//2] == n[-(len(n)//2):][::-1]

def closest_palindrome(num):
	n1, n2 = num, num
	while True:
		if ft_aid(n1):
			return n1
		elif ft_aid(n2):
			return n2
		n1 -= 1
		n2 += 1
