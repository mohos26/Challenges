# https://edabit.com/challenge/J67xWvM4jFhn9nEpJ

def is_magic(size):
    pass

'''def ist(n):
    res = 19
    for i in range(1, n):
        res += 9 + 3 * i
    return res

def ist2(n):
    res = 15
    for i in range(1, n):
        res += ist(i)
    return res
'''
def ist(n):
    return n*(n**2+1)//2

def ist3(lst, n):
    result = []
    pass

def is_magic(n):
    base = ist(n)


def idigin(lst):
	lst2 = []
	for i in range(n):
		lst2.append(lst[i*n:(i+1)*n])
	res = [], []
	for i in lst2[1:-1]:
		res[0].append(i[-1])
		res[1].append(i[0])
	return lst2[0] + res[0] + lst2[-1][::-1] + res[1][::-1]


def idigin2(lst, n):
	return lst[-n:] + lst[:-n]

print(idigin2([1, 2, 3, 4], 1))
