# https://edabit.com/challenge/uHcc8Gg4jwSax5qd4
# 19.02.2025
# Very Hard


class Minecart:

	def __init__(self, v=0):
		self.v = v

		if self.v <= 0:
			self.im = False
		else:
			self.im = True

	def add_speed(self, speed):

		if self.im == False:
			self.im = True

		if self.v + speed <= 8 and self.v + speed > 0:
			self.v += speed
		elif self.v + speed <= 0:
			self.v = 0
			self.im = False
		else:
			self.v = 8

d = {
	"<--": -2.67,
	"-->": 2.67,
	"<-->": 0,
	"---": -1
}

def mine_run(tracks):
	i = 0
	mine = Minecart(d[tracks[0]])
	for arg in tracks[1:]:
		if not mine.im:
			return i
		mine.add_speed(d[arg])
		i += 1
	return True
