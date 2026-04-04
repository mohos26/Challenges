# https://leetcode.com/problems/available-captures-for-rook/
# 04.04.2026


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        res = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    x, y = i, j
                    break
        directions = (-1, 0), (1, 0), (0, 1), (0, -1)
        for a, b in directions:
            dx, dy = x, y
            while 0 <= dx+a < 8 and 0 <= dy+b < 8:
                dx, dy = dx+a, dy+b
                if board[dx][dy] == 'p':
                    res += 1
                    break
                elif board[dx][dy] != '.':
                    break
        return res

