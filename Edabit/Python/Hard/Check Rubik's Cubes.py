# https://edabit.com/challenge/PLdJr4S9LoKHHjDJC
# 18.06.2025
# Very Hard


def identify(*cube):
	row = len(cube)
	column = len(max(cube, key=len))
	length = 0
	for arg in cube:
		length += len(arg)
	if row * column != length:
		return f"Missing {row * column - length}"
	elif row != column:
		return "Non-Full"
	return "Full"
