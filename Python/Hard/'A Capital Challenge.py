# https://edabit.com/challenge/eBTCwYHpdaHciieuP
# 02.05.2025
# Hard


def select_letters(s1, s2):
	res = ""
	for i in range(len(s2)):
		if s2[i].isupper():
			res += s1[i]
	for i in range(len(s2)):
		if s1[i].isupper():
			res += s2[i]
	return res
