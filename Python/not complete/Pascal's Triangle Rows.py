# https://edabit.com/challenge/ENxiMBnKzf5HQgin2
# 23.08.2023
# Expect


# def pascal_row(n):
# 	lst = [[1]]
# 	for i in range(1, n + 1):
# 		lst.append([1] + [0] * (i - 1) + [1])
# 		for j in range(1, i):
# 			lst[i][j] = lst[i - 1][j - 1] + lst[i - 1][j]
# 	return lst[n]

# def pascal_row_remaster(n):
#     """lst = [1]
#     if n == 0:
#         return lst
#     for i in range(1, (n + 1) // 2):
#         # ((1 + ((1 / i) * (n - (2 * i - 1)))) * (lst[-1] / n)) * n
#         lst.append(lst[-1]*((n-i+1)/i))
#     if n % 2 == 0:
#         i = n // 2
#         return lst + [lst[-1]*((n-i+1)/i)] + lst[::-1]
#     return lst + lst[::-1]"""
#     if n == 0:
#         return [1]

#     row = [1]
#     for i in range(1, (n + 1) // 2):
#         new_value = int(row[-1] * (n - i + 1) / i)
#         row.append(new_value)

#     if n % 2 == 0:
#         middle_value = int(row[-1] * ((n - (n // 2) - 1) / (n // 2)))
#         return row + [middle_value] + row[::-1]

#     return row + row[::-1]

# def pascal_row_new(n):
# 	if n % 2:
# 		return False
# 	res = []
# 	aid = None
# 	aid2 = None
# 	for i in range(n//2):
# 		if aid == None:
# 			res.append(1)
# 			aid = n - 1
# 		else:
# 			res.append(aid)
# 			aid += (n - 1) * i
# 	return res

# for i in range(2, 17, 2):
# 	print(*pascal_row_new(i))

def pascal_row(n):
	res, lst2 = [1], []
	aid = []
	aid2 = n -1
	lst = [1] * (n)
	for i in range(n - 1, (n - 1) // 2 + ((n - 1) % 2), -1):
		for j in range(i + 1):
			if not j:
				lst2.append(lst[j])
			else:
				lst2.append(lst2[-1] + lst[j])
		res.append(lst2[-1])
		lst = lst2
		lst2 = []
	else:
		if (n-1) % 2:
			for j in range(i):
				if not j:
					lst2.append(lst[j])
				else:
					lst2.append(lst2[-1] + lst[j])
			aid.append(lst2[-1])
	return res + aid + res[::-1]

# lst = 1, 1, 1, 1, 1, 1, 1, 1

# lst2 = []

# for i in range(len(lst)):
# 	if not i:
# 		lst2.append(lst[i])
# 	else:
# 		lst2.append(lst2[-1] + lst[i])


print(pascal_row(5))
print(pascal_row(10))
