# https://edabit.com/challenge/PirFJDfGk4vpsdkeE
# 14.05.2025
# Vary Hard


def help_bobby(size):
	array=[]
	for arg in [[0]*size]*size:array.append(arg.copy())
	for i in array:print(i)
	row=0
	for column in range(size):
		array[column][row]=1
		array[column][size-row-1]=1
		row+=1
	for i in array:print(i)
	return array


def my_help_bobby(size):
	res = []
	for arg in [[0]*size]*size:
		res.append(arg.copy())
	for i in range(size):
		res[i][i] = 1
		res[i][size-i-1] = 1
	return res
