# https://leetcode.com/problems/word-search
# 11.01.2026


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        w, h = len(board), len(board[0])

        def dfs(nn, n):
            if nn == len(word):
                return True
            i, j = n // h, n % h
            for a, b in ((i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)):
                if 0 <= a < w and 0 <= b < h and word[nn] == board[a][b]:
                    board[a][b] = None
                    if dfs(nn + 1, a * h + b):
                        return True
                    board[a][b] = word[nn]
            return False

        for i in range(w):
            for j in range(h):
                if board[i][j] == word[0]:
                    board[i][j] = None
                    if dfs(1, i * h + j):
                        return True
                    board[i][j] = word[0]

        return False

