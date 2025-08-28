# https://edabit.com/challenge/zeuvB4YRvu47w8e8f
# 19.05.2025
# Very Hard


def full_cycle(lst):
	i = 0
	length = 0
	while length < len(lst):
		if i >= len(lst) or lst[i] == -1:
			return False
		tmp = i
		i = lst[i]
		lst[tmp] = -1
		length += 1
	return True
