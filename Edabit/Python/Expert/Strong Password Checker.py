# https://edabit.com/challenge/H2NCAro2tdbGavzg7
# 01.12.2024
# Expect


def faid(txt):
	lst = [0, 0, 0]
	for letter in txt:
		if not lst[0] and letter.islower():
			lst[0] = 1
		elif not lst[1] and letter.isdigit():
			lst[1] = 1
		elif not lst[2] and letter.isupper():
			lst[2] = 1
	return 3 - sum(lst)

def faid2(txt):
	lst = []
	aid = None
	for letter in txt:
		if aid == letter:
			lst[-1] += 1
		else:
			lst.append(1)
		aid = letter
	aid = len(txt) - 20
	aid *= aid > 0
	lst2 = []
	for i in lst:
		if i > 2:
			lst2.append(i)
	while sum(lst2) and aid:
		lst2.sort(key=lambda n: n%3)
		lst2[0] -= 1
		aid -= 1
	return sum(map(lambda x: x // 3, lst2))

def password_checker(txt):
	res = max(faid(txt), faid2(txt))
	if len(txt) > 20:
		res += len(txt) - 20
	elif len(txt) < 8:
			res = max(8 - len(txt), res)
	return res
