# https://edabit.com/challenge/6hnrKRh7fZfMC5CKY
# 08.05.2025
# Hard


def look_and_say(n):
	n = str(n)
	if len(n) % 2:
		return "invalid"
	res = ""
	for i in range(0, len(n), 2):
		res += int(n[i]) * n[i + 1]
	return int(res)
