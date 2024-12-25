# https://edabit.com/challenge/dWeA6vWdrPYtwhxoS
# Medium
# 17.10.2024


def count_number(lst):
	if not lst:
		return 0
	elif type(lst[0]) is list:
		return count_number(lst[0] + lst[1:])
	return (type(lst[0]) in (int, float)) + count_number(lst[1:])

