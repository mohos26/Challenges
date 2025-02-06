# https://edabit.com/challenge/vLRpikwB9dqaR3HAj
# Hard
# 21.08.2024


def is_ord_sub(smlst, biglst):
	for i in smlst:
		if i in biglst:
			biglst = biglst[biglst.index(i)+1:]
		else:
			return False
	return True

