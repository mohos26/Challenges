# https://edabit.com/challenge/XjgoXNmnz59txiQp3
# 18.08.2023 -> 06.02.2025
# Very Hard

def split(n):
	aid = n//3
	if n - aid * 3 == 1 and aid:
		aid -= 1
	aid2 = n-aid*3
	if not aid2:
		aid2 = 1
	return 3**aid * aid2
