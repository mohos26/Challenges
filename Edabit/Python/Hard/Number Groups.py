# https://edabit.com/challenge/SYmHGXX2P26xu7JFR
# 14.05.2025
# Hard


def number_groups(group1, group2, group3):
	res = []
	for n in set(group1 + group2 + group3):
		if (n in  group1) + (n in group2) + (n in group3) >= 2:
			res.append(n)
	return res
