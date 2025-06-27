# https://edabit.com/challenge/J9wWjJXT9MLvosN4F
# 13.06.2025
# Hard


def pad_matrix(matrix):
	res = []
	row = 2 + len(matrix)
	column = 2 + len(matrix[0])
	for _ in range(row):
		res.append([0] * column)
	for i, arg in enumerate(matrix):
		for j, arg2 in enumerate(arg):
			res[i + 1][j + 1] = arg2
	return res
