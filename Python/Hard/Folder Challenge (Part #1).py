# https://edabit.com/challenge/9yk63KrKDHzNFWKBJ
# 25.06.2025
# Very Hard


def is_it_inside(folders, X, Y):
	if X == Y:
		return True
	if Y in folders.keys():
		lst = folders[Y]
		if X in lst:
			return True
		for arg in lst:
			if is_it_inside(folders, X, arg):
				return True
	return False
