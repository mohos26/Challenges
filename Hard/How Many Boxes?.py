# https://edabit.com/challenge/QdEAMeXNJAivcTMiT
# 17.02.2025
# Hard


def boxes(weights):
	res = 0
	i = 0
	lst = []
	while i < len(weights):
		if weights[i] <= 10:
			if lst and sum(lst) + weights[i] <= 10:
				lst.append(weights[i])
			elif not lst:
				res += 1
				lst.append(weights[i])
			else:
				lst = []
				i -= 1
		else:
			lst = []
		i += 1
	return res
