# https://edabit.com/challenge/aQWPiDnfwdE7xnqDq
# Very Hard
# 05.09.2024


def drange(*args):
	result = []
	if len(args) > 2:
		start, end, step = args[:3]
	elif len(args) == 2:
		start, end, step = *args, 1
	else:
		start, end, step = 0, *args, 1
	var = start
	while var < end:
		result.append(round(var, 6))
		var += step
	return tuple(result)

print(drange(1.2, 5.9, 0.45))
print(drange(10))
print(drange(1, 7, 1.2))
