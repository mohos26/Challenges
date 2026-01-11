# https://leetcode.com/problems/game-of-life
# 22.11.2026


class Solution:
    def ft_aid(self, board, x, y):
        sum_v = 0
        m, n = len(board), len(board[0])
        lst = [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]
        for a, b in lst:
            if 0 <= a < m and 0 <= b < n and board[a][b]:
                sum_v += 1
        if sum_v < 2 or sum_v > 3:
            return 0
        if board[x][y] and 2 <= sum_v <= 3:
            return 1
        return int(sum_v == 3)


    def gameOfLife(self, board: List[List[int]]) -> None:
        board_copy = deepcopy(board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = self.ft_aid(board_copy, i, j)

