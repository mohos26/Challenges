# https://edabit.com/challenge/MFFuPFnjT8ihniKtL
# 22.03.2024 -> 08.02.2025
# Very Hard


def bug_jump(height, time):
	time = time/1000
	t = 2*(height**0.5)
	m = round(-(time**2) + t*time, 2)
	if m <= 0 and time > t:
		return [0, None]
	return [m, ('up', 'down')[t/2 < time]]
