# https://edabit.com/challenge/hS2g8KDw2sk6QjKgb
# 03.05.2025
# Expert


def moving_particles(lst):
	res = []
	for i in lst:
		if res and res[-1] > 0 and i < 0:
			aid = res[-1] + abs(i)
			if res[-1] < abs(i):
				aid *= -1
			res[-1] = aid
		else:
			res.append(i)
	if res == lst:
		return res
	return moving_particles(res)
