# https://edabit.com/challenge/DqLngKnnJcZyPMctn
# 19.07.2023
# Hard


def stock_picker(lst):
	lst2 = []
	for i, arg in enumerate(lst[:-1]):
		for j in lst[i+1:]:
			lst2.append(j - arg)
	res = sorted(lst2)[-1]
	if res < 0:
		res = -1
	return res
