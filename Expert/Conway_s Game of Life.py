# https://edabit.com/challenge/cHzvB5KCWCK3oCLGL
# 2.09.2023
# Expect


def game_of_life(board):
    result = ''
    for i, line in enumerate(board):
        for ii, arg in enumerate(line):
            num = 0
            for j in [(i-1, ii-1), (i-1, ii), (i-1, ii+1), (i, ii-1), (i, ii+1), (i+1, ii-1), (i+1, ii), (i+1, ii+1)]:
                if -1 < j[0] < len(board) and -1 < j[1] < len(line) and board[j[0]][j[1]] == 1:
                    num += 1
            if (arg == 1 and 1 < num < 4) or (arg == 0 and num == 3):
                result += 'I'
            else:
                result += '_'
        result += '\n'
    return result[:-1]
