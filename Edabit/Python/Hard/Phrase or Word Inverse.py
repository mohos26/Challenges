# https://edabit.com/challenge/ThvNE5FZRX6JbGoTo
# 21.10.2024
# hard

def inverter(txt, type):
	aid = txt.lower().split()
	if type == 'W':
		return ' '.join(map(lambda s: s[::-1], aid)).capitalize()
	return ' '.join(aid[::-1]).capitalize()

