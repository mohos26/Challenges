# https://edabit.com/challenge/tRHaoWNaHBJCYD5Nx
# Very Hard
# 03.09.2024


def remove_duplicate(txt):
	result = []
	for i in txt:
		if i not in result:
			result.append(i)
	return result

def same_letter_pattern(txt1, txt2):
	lst = [remove_duplicate(txt1), remove_duplicate(txt2)]
	result = ''
	# check if length of txt1 equal txt2
	if not(len(lst[0]) - len(lst[1])):
		for i in txt1:
			result += lst[1][lst[0].index(i)]
	return txt2 == result

