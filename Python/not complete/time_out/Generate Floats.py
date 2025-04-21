# https://edabit.com/challenge/HhSS3YReRhBxZAnzk
# 03.08.2023
# Medium

from math import ceil

def gen_values(n, i):
	result, var = [], 0
	while var <= n:
		result.append(var)
		var = round(var+i, len(str(i))-2)
	return result

print(gen_values(1, 0.04))
