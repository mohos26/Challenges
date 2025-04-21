# https://edabit.com/challenge/ZvjGe7dQAbvbxoPGZ
# 4.11.2023
# Very Hard


def rgb_or_hex(*args):
	if type(args[0]) == str:
		return int(f'0x{args[0][1:3]}', 16), int(f'0x{args[0][3:5]}', 16), int(f'0x{args[0][5:]}', 16)
	return f'#{hex(args[0])[2:]}{hex(args[1])[2:]}{hex(args[2])[2:]}'
