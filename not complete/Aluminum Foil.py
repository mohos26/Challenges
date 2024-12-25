# https://edabit.com/challenge/siuKPSYXjjic9zEF2
# 3.11.2023
# Expect


from math import pi


def foil(length):
	var = 4
	while length > 0:
		var += 0.0025
		var2 = pi * var
		length -= var2
		length = round(length, 4)
	return var
