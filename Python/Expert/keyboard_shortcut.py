# https://edabit.com/challenge/6Ran7nuFijxkXD95o
# 31.1.2023 -> 08.02.2025
# Expert


def ft_split(txt):
	lst2 = []
	aid = txt
	while aid.count("Ctrl + "):
		aid = aid[aid.index("Ctrl + ")+7:]
		lst2.append(aid[0])
		aid = aid[1:]
	return txt.replace("Ctrl + V", "Ctrl + C").split("Ctrl + C"), lst2

def ft_add(s, s2):
	return (s.strip() + " " + s2.strip()).strip()

def keyboard_shortcut(txt):
	res, aid, i = "", "", 0
	lst = ft_split(txt)
	for arg in lst[0][:-1]:
		res = ft_add(res, arg)
		if lst[1][i] == 'C':
			aid = res
		else:
			res = ft_add(res, aid)
		i += 1
	return ft_add(res, lst[0][-1])
