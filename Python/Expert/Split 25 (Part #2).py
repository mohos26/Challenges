# 06.02.2024

from math import exp, ceil

def split(x):
	aid = x / exp(1)
	if not int(aid):
		aid = 1
	return max(round((x/ceil(aid))**ceil(aid), 1), round((x/int(aid))**int(aid), 1))