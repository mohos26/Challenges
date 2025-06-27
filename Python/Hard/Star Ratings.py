# https://edabit.com/challenge/2fZETLANpgp6uhTjG
# 27.06.2025
# Hard


def ft_aid(n):
	nn = str(n)
	if len(nn[nn.index('.') + 1:]) != 2:
		nn += '0'
	return nn

def star_rating(lst):
	aid = 0
	for i, n in enumerate(lst):
		aid += n * (i + 1)
	aid = round(aid / sum(lst), 2)
	return '[' + str(ft_aid(aid)) + ']' + ' ' + '*' * round(aid)
