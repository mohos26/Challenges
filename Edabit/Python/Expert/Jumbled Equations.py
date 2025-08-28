# https://edabit.com/challenge/RgdAjTADFg2r4wne3
# 25.06.2025
# Expert


def jumbled(lst):
	res = []
	pairs = []
	numbers = lst[1]
	operators = lst[0]
	for i in numbers:
		for j in numbers:
			if j != i:
				pairs.append([i, j])
	for operator in operators:
		for a, b in pairs:
			result = eval(f'{a}{operator}{b}')
			if result == int(result):
				result = int(result)
			if result in numbers and result not in (a, b):
				if result == eval(f'{b}{operator}{a}') and operator != '**':
					expr = f"{min(a, b)}{operator}{max(a, b)}={result}"
					if expr not in res:
						res.append(expr)
				else:
					res.append(f"{a}{operator}{b}={result}")
	return sorted(res)
