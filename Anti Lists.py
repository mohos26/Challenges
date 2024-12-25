# https://edabit.com/challenge/TDrfRh63jMCmqzGjv
# 13.07.2023 -> 04.12.2024
# Medium


def is_anti_list(lst1, lst2):
	for i in range(len(lst1)):
		if lst1[i] == lst2[i]:
			return False
	return set(lst1) == set(lst2)
