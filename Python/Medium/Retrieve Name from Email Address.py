# https://edabit.com/challenge/pDmDP9KhXmBTcScT6
# 07.05.2025
# Medium


def get_name(address):
	name = address.split('@')[0]
	res = ""
	for i in name:
		if i.isalpha():
			res += i
	return res
