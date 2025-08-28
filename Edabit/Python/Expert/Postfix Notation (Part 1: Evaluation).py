# https://edabit.com/challenge/xWW8PMuLN8hmAgLMJ
# 22.08.2025
# Very Hard


def is_operator(s):
	return s in ("/", "*", "-", "+")


def postfix(expression):
	lst = expression.split()
	stack = []
	for arg in lst:
		if is_operator(arg):
			b, a = stack.pop(), stack.pop()
			stack.append(str(int(eval(a + arg + b))))
		else:
			stack.append(arg)
	return int(stack.pop())
