# https://edabit.com/challenge/s89T6kpDGf8Pc6mzf
# 08.05.2025
# very Hard


d = {
	'0': "abcdef",
	'1': "bc",
	'2': "abdeg",
	'3': "abcdg",
	'4': "bcfg",
	'5': "acdfg",
	'6': "acdefg",
	'7': "abc",
	'8': "abcdefg",
	'9': "abcfg",
}

def ft_aid(n):
	lst = []
	for i in n:
		lst.append(list(d[i]))
	return lst

def seven_segment(txt):
	lst = ft_aid(txt)
	res = []
	for i in range(1, len(lst)):
		l1 = lst[i-1].copy()
		l2 = lst[i].copy()
		j = 0
		while j < len(l1):
			if l1[j] in l2:
				l2.remove(l1[j])
				l1.remove(l1[j])
			else:
				j += 1
		l2 = list(map(str.upper, l2))
		res.append(sorted(l1 + l2, key=str.lower))
	return res
