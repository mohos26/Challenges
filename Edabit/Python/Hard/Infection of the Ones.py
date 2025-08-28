# https://edabit.com/challenge/tY5fmSbk85N8digXQ
# 02.05.2025
# Very Hard


def get_indices(lst, el, row):
	res = []
	while el in lst:
		aid = lst.index(el)
		res.append([aid // row, aid % row])
		lst[lst.index(el)] = 0
	return res

def ones_infection(arr):
	column = len(arr)
	row = len(arr[0])
	lst = []
	for arg in arr:
		lst += arg
	for arg in get_indices(lst, 1, row):
		for i in range(row):
			arr[arg[0]][i] = 1
		for i in range(column):
			arr[i][arg[1]] = 1
	return arr
