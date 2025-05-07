# https://edabit.com/challenge/6b8Px5m82nAgudhsy
# 07.05.2025
# Expert


from itertools import permutations

def next_number(num):
	lst = sorted(set((map(int, map(lambda l: ''.join(l), permutations(str(num)))))))
	aid = lst.index(num)
	if len(lst) >= aid + 1:
		return lst[aid + 1]
	return (num)

def ft_aid(s):
	s, aid = list(s), s[-1]
	for i in sorted(s):
		if i > aid:
			s.remove(i)
			return "".join(sorted(s)[::-1] + [i])

def next_number_bonus(num):
	res, num = "", str(num)
	for i, n in enumerate(num[::-1]):
		if res and n < res[-1]:
			res = ft_aid(res + n) + num[:-i-1]
			break
		else:
			res += n
	return int(res[::-1])
