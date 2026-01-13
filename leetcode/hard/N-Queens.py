# https://leetcode.com/problems/n-queens
# 29.08.2025


class Solution:
    def ft_aid(self, board: List[List[str]], n: int, x: int, y: int) -> List[Tuple[int]]:
        res = []
        board[x][y] = 'Q'
        for step in range(1, n + 1):
            for i, j in ((x, y + step), (x, y - step), (x + step, y), (x - step, y), (x + step, y + step), (x + step, y - step), (x - step, y - step), (x - step, y + step)):
                if 0 <= i < n and 0 <= j < n and board[i][j] == '.':
                    res.append((i, j))
                    board[i][j] = 'x'
        return res


    def dfs(self, board: List[List[str]], res, n: int, N:int):
        if not n:
            res.append([arg[:] for arg in board])
            return
        lst2 = []
        for i, line in enumerate(board):
            if 'Q' in line:
                continue
            for j, arg in enumerate(line):
                if arg == '.':
                    lst = self.ft_aid(board, N, i, j)
                    self.dfs(board, res, n-1, N)
                    for x, y in lst:
                        board[x][y] = '.'
                    board[i][j] = 'x'
                    lst2.append((i, j))
        for x, y in lst2:
            board[x][y] = '.'


    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for _ in range(n)]
        self.dfs(board, res, n, n)
        for i in range(len(res)):
            for j in range(n):
                res[i][j] = ''.join(res[i][j])
                res[i][j] = res[i][j].replace('x', '.')
        return res



# 13.01.2026
class Solution:
    # 0: void, 1: queen area, 2: queen
    def ft_aid(self, board, i, j):
        lst = []
        n = len(board)
        for d in range(1, n):
            lst.append((i+d, j))
            lst.append((i-d, j))
            lst.append((i, j+d))
            lst.append((i, j-d))
            lst.append((i+d, j+d))
            lst.append((i-d, j-d))
            lst.append((i+d, j-d))
            lst.append((i-d, j+d))
        res = []
        for a, b in lst:
            if 0 <= a < n and 0 <= b < n and board[a][b] == 0:
                res.append((a, b))
                board[a][b] = 1
        return res

    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [[0] * n for _ in range(n)]
        def dfs(i):
            if i == n:
                lst = []
                for arg in board:
                    lst.append(''.join('Q' if i == 2 else '.' for i in arg))
                res.append(lst)
                return
            for j in range(n):
                if board[i][j] == 0:
                    lst = self.ft_aid(board, i, j)
                    board[i][j] = 2
                    dfs(i+1)
                    board[i][j] = 0
                    for a, b in lst:
                        board[a][b] = 0
        dfs(0)
        return res

