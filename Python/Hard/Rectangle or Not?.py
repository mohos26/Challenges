# https://edabit.com/challenge/es6qJTs5zYf8nEBkG
# 11.05.2025
# Very Hard


def is_rectangle(coordinates):
	aid = 0
	if len(coordinates) != 4:
		return False
	for i in range(4):
		coordinates[i] = list(map(int, coordinates[i][1:-1].replace(' ', '').split(',')))
	while coordinates:
		if len(coordinates) == 4:
			aid = [coordinates[0][0], 0]
			coordinates.pop(0)
		else:
			for a, b in coordinates:
				if aid[1]:
					if b == aid[0]:
						coordinates.remove([a, b])
						aid = [a, 0]
						break
				else:
					if a == aid[0]:
						coordinates.remove([a, b])
						aid = [b, 1]
						break
			else:
				return False
	return True
