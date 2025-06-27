# https://edabit.com/challenge/rbeuWab36FAiLj65m
# 13.06.2025
# Very hard


def grouping(words):
	res = {}
	for word in words:
		aid = sum(map(str.isupper, word))
		if aid not in res.keys():
			res.update({aid: [word]})
		else:
			res[aid].append(word)
	# sorted alphabetically (ignoring case)
	for key in res.keys():
		res[key] = sorted(res[key], key=str.lower)
	return res
