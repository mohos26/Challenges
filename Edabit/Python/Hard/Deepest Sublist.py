# https://edabit.com/challenge/iLLqX4nC2HT2xxg3F
# Very Hard
# 12.03.2025


def deepest(lst):
	res = 1
	for i in lst:
		if type(i) == list:
			aid = 1 + deepest(i)
			if aid > res:
				res = aid
	return res
