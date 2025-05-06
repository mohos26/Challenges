# https://edabit.com/challenge/qYrTDRY7AN2RHxvXg
# 05.05.2025
# Expert


from math import sqrt


def f(A, c):
	try:
		a = round(sqrt((c**2 -sqrt(c**4 -16 * A**2)) / 2), 3)
		b = round(sqrt((c**2 + sqrt(c**4 -16 * A**2)) / 2), 3)
		return [a, b]
	except:
		return "Does not exist"
