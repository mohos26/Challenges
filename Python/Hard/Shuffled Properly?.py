# https://edabit.com/challenge/XALogvSrMr3LRwXPH
# 11.05.2025
# Hard


def ft_aid(lst, lst2, i):
	for j, n in enumerate(lst2):
		if n != lst[i + j]:
			break
	else:
		return True
	return False

def is_shuffled_well(lst):
	for i, n in enumerate(lst[:-2]):
		if ft_aid(lst, range(n, n+3, 1), i) or ft_aid(lst, range(n, n-3, -1), i):
			return False
	return True
