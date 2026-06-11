# https://leetcode.com/problems/set-matrix-zeroes/
# 11.06.2026


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeros = []
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeros.append((i, j))
        for a, b in zeros:
            for i in range(m):
                matrix[i][b] = 0
            for i in range(n):
                matrix[a][i] = 0

