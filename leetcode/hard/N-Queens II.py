# https://leetcode.com/problems/n-queens-ii/
# 18.01.2026


class Solution:
    def ft_aid(self, board, i, j):
        lst = []
        n = len(board)
        for a in range(n):
            lst.append((i + a, j))
            lst.append((i, j + a))
            lst.append((i + a, j + a))
            lst.append((i - a, j))
            lst.append((i, j - a))
            lst.append((i - a, j - a))
            lst.append((i + a, j - a))
            lst.append((i - a, j + a))
        res = []
        for a, b in lst:
            if i+1 <= a < n and 0 <= b < n and board[a][b] == 0:
                res.append((a, b))
                board[a][b] = 1
        return res

    def totalNQueens(self, n: int) -> int:
        res = 0
        board = [[0] * n for _ in range(n-1)]

        def dfs(i):
            if i == n:
                nonlocal res
                res += 1
                return
            for j in range(n):
                if board[i][j] == 0:
                    tmp = self.ft_aid(board, i, j)
                    dfs(i + 1)
                    for a, b in tmp:
                        board[a][b] = 0

        for i in range(n):
            tmp = self.ft_aid(board, 0, i)
            dfs(1)
            for a, b in tmp:
                board[a][b] = 0
        return res

