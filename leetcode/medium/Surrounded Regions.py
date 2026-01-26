# https://leetcode.com/problems/surrounded-regions/
# 25.01.2026


class Solution:
    def surrounded(self, i, j, N, M):
        return i == 0 or i == N - 1 or j == 0 or j == M - 1

    def solve(self, board: List[List[str]]) -> None:
        N, M = len(board), len(board[0])
        res = []

        def dfs(i, j):
            board[i][j] = 'X'
            res[-1][1].append((i, j))
            if self.surrounded(i, j, N, M):
                res[-1][0] = True
            for a, b in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= a < N and 0 <= b < M and board[a][b] == "O":
                    dfs(a, b)

        for i in range(N):
            for j in range(M):
                if board[i][j] == "O":
                    res.append([False, []])
                    dfs(i, j)
                    if not res[-1][0]:
                        res.pop()
        for _, lst in res:
            for a, b in lst:
                board[a][b] = "O"

