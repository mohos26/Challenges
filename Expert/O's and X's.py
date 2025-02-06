# https://edabit.com/challenge/66xK46dhKFCe5REDg
# 10.11.2024
# Expect


def x_and_o(board):
    answer = [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]
    board, lst = ('|'.join(board)).split('|'), []
    for i in range(9):
        if board[i] == 'X':
            lst.append(i)
    print(lst)
    for i in answer:
        aid = 0
        for j in i:
            if j in lst:
                aid += 1
        if aid == 2:
            for j in i:
                if j not in lst and board[j] == ' ':
                    return [j//3+1, j%3+1]
    return False

print(x_and_o(board = [" | | ", "X|X| ", " | | "]))