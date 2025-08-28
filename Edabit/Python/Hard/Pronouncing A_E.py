# https://edabit.com/challenge/vZDgbWkcevrwzLh8W
# 27.06.2025
# Hard

def pronounce_the_a_e(txt):
	i = 0
	res, buffer = "", ""
	while i < len(txt):
		if buffer and txt[i] == 'e':
			res += 'ay' + buffer[1:]
			buffer = ''
		elif buffer and txt[i] == ' ':
			i -= len(buffer)
			res += buffer
			buffer = ''
		elif buffer:
			buffer += txt[i]
		elif txt[i] == 'a':
			buffer = 'a'
		else:
			res += txt[i]
		i += 1
	return res + buffer
