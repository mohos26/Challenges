# https://edabit.com/challenge/6vSZmN66xhMRDX8YT
# 04.03.2023 -> 04.12.2024
# Very Hard


def advanced_sort(lst):
	res, lst2 = [], []
	for item in lst:
		if not item in lst2:
			res.append([item]*lst.count(item))
			lst2.append(item)
	return res
