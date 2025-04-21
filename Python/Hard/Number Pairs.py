# https://edabit.com/challenge/rMwssAueJjn9FmjZC
# 15.06.2024 -> 08.02.2025
# Hard

def number_pairs_(txt):
	res = 0
	lst = list(map(int, txt.split()))[1:]
	for i in list(set(lst)):
		res += lst.count(i)//2
	return res
