from math import ceil, floor

with open('/tmp/input.txt') as file:
	start, result = 50, 0
	while (line := file.readline().strip()):
		sing = 1
		if line[0] == 'L':
			sing = -1
		num = int(line[1:]) * sing
		start += num

		if start < 0:
			result += abs(ceil(start / 100))
			if start - num > 0:
				result +=  1
		elif start > 0:
			result += floor(start / 100)
		else:
			result += 1

		if start < 0:
			start += ceil(start / 100) * 100
		start %= 100

	print(result)
