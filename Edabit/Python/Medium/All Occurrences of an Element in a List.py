# https://edabit.com/challenge/jwzgYjymYK7Gmro93
# 01.05.2024
# Meduim


def get_indices(lst, el):
	res = []
	while el in lst:
		res.append(lst.index(el))
		lst[lst.index(el)] = None
	return res
