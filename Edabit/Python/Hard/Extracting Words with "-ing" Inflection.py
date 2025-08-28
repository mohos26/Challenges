# https://edabit.com/challenge/xxqSGobjKXo3hDM4h
# 06.05.2025
# Very Hard


def ft_aid(s):
	for letter in s:
		if letter in 'euioa':
			return True
	return False

def ing_extractor(string):
	res = []
	for word in string.split():
		if word.lower()[-3:] == "ing" and len(word) > 4 and ft_aid(word[:-3].lower()):
			res.append(word)
	return res
