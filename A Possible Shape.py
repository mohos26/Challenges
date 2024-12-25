# https://edabit.com/challenge/K4aKGbfmzgyNNYEcM
# 08.09.2023
# Medium


def is_shape_possible(n, angles):
    for angle in angles:
        if 0 > angle > 179:
            return False
    return sum(angles) == (n - 2) * 180


# 04.12.2024

def is_shape_possible_fix(n, angles):
	if n < 3:
		return False
	for angle in angles:
		if 0 > angle > 179:
			return False
	if n == 3:
		return sum(angles) == (n - 2) * 180
	return angles.count(angles[0]) == n and angles[0]* n == (n - 2) * 180
