# https://edabit.com/challenge/pa7tTr3g4XaNkHoWC
# 06.05.2025
# Hard


def pig_latin_sentence(sentence):
	res, d = [], {0: "", 1: "way", 2: "ay"}
	for word in sentence.split():
		part_one, part_two, flag = "", "", 0
		for i, letter in enumerate(word):
			if letter in "euioa" or flag:
				part_two += letter
				if not flag:
					flag = 2
					if not i:
						flag = 1
			else:
				part_one += letter
		res.append(part_two + part_one + d[flag])
	return ' '.join(res)
