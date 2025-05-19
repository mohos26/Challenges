# https://edabit.com/challenge/7vN8ZRw43yuWNoy3Y
# 09.05.2025
# Hard


def parse_code(txt):
	lst = []
	for arg in txt.split('0'):
		if arg:
			lst.append(arg)
	d = {
		"first_name": lst[0],
		"last_name": lst[1],
		"id": lst[2]
	}
	return d
