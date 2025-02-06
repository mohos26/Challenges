# https://edabit.com/challenge/vudQZFD64nDWkKz8a
# 02.12.2024
# very Hard


def _aid(word, n):
	aid2 = len(word) * '_'
	n = min(n, len(word))
	return word[:n] + aid2[n:]

def grant_the_hint(txt):
	res = []
	lst = txt.split()
	max_len = len(max(lst, key=lambda word: len(word)))
	for i in range(max_len+1):
		res.append([])
		for word in lst:
			res[-1].append(_aid(word, i))
		res[-1] = ' '.join(res[-1])
	return res
