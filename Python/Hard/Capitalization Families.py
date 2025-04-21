# https://edabit.com/challenge/rbeuWab36FAiLj65m
# 27.11.2024
# Very Hard


def grouping(lst):
	res = dict()
	for word in lst:
		aid = 0
		for letter in word:
			if letter.isupper():
				aid += 1
		if aid in res.keys():
			res[aid].append(word)
			res[aid].sort(key=lambda x: x.lower())
		else:
			res.update({aid: [word]})
	return res
