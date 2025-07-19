# https://edabit.com/challenge/HaMCeHeJkaWvMg7LS
# 19.07.2025
# Very Hard


def sun_loungers(beach):
	if len(set(beach)) == 1 and beach[0] == '0':
		return (len(beach) + 1) // 2
	res, aid, start = 0, 0, True
	for arg in beach:
		if arg == '0':
			aid += 1
		else:
			if start:
				res += aid // 2
			elif aid:
				res += (aid - 1) // 2
			start = False
			aid = 0
	return res + aid // 2
