# https://edabit.com/challenge/4wJc7maZhYCSgzyRS
# 03.06.2025
# Very Hard


def two_product(lst, N):
	for n in lst:
		print(N, n, N / n)
		if N / n in lst:
			return [n, N // n]
	return None

""" why [100, 1872] is the answer for the last test?
There are three solutions, with the first solution being [72, 2600]:
Solution 1: [72, 2600], index = (431, 2238)
Solution 2: [720, 260], index = (647, 2935)
Solution 3: [100, 1872], index = (806, 926)
Is there a specific order that we need to take into account? """
