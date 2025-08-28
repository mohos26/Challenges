# https://edabit.com/challenge/NZtL4MGkpCfiwShhp
# 26.08.2025
# Expert


d = {
	"/": 2,
	"*": 2,
	"**": 3,
	"-": 1,
	"+": 1,
}

def is_operator(s):
	return s in ("/", "*", "-", "+", "**", "(", ")")


def ft_aid(expr):
	stack = []
	postfix = []
	while expr:
		arg = expr[0]
		if is_operator(arg):
			if arg == ')':
				while stack[-1] != '(':
					postfix.append(stack.pop())
				expr = expr[1:]
				stack.pop()
			elif not stack or '(' in (arg, stack[-1]) or d[stack[-1]] < d[arg]:
				stack.append(arg)
				expr = expr[1:]
			else:
				postfix.append(stack.pop())
		else:
			postfix.append(arg)
			expr = expr[1:]
	while stack:
		postfix.append(stack.pop())
	return postfix


def ft_parsing(s):
	res = []
	aid = ""
	for arg in s:
		if arg.isspace():
			if aid:
				res.append(aid)
				aid = ""
		elif is_operator(arg):
			if aid and not is_operator(aid):
				res.append(aid)
				aid = ""
			if aid and is_operator(aid + arg):
				aid += arg
			else:
				if aid:
					res.append(aid)
				aid = arg
		else:
			if is_operator(aid):
				res.append(aid)
				aid = ""
			aid += arg
	if aid:
		res.append(aid)
	return res


def infix_to_postfix(expr):
	expr = ft_parsing(expr)
	postfix = ft_aid(expr)
	return ' '.join(postfix)
