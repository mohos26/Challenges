# https://edabit.com/challenge/FT5Zd4mayPa5ghpPt
# 27.06.2025
# Very Hard


def ft_hex_valid(h):
	if len(h) != 6:
		return False
	for i in h:
		if i not in "0123456789abcdef":
			return False
	return True

def ft_dict_valid(d):
	for key, n in d.items():
		if n > 255 or 0 > n:
			return False
	return True

def color_conversion(h):
	if type(h) == dict:
		if not ft_dict_valid(h):
			return "Invalid input!"
		return '#' + hex(h['r'])[2:].zfill(2) + hex(h['g'])[2:].zfill(2) + hex(h['b'])[2:].zfill(2)
	if h[0] == '#':
		h = h[1:]
	if not ft_hex_valid(h):
		return "Invalid input!"
	return {'r': int(h[:2], 16), 'g': int(h[2:4], 16), 'b': int(h[4:6], 16)}
