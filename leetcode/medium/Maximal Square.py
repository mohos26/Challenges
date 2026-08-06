# https://leetcode.com/problems/maximal-square/
# 06.08.2026


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    res = 1
                    break
            else:
                continue
            break
        else:
            return 0
        dp = [[0] * n for _ in range(m)]
        for i in range(n):
            dp[0][i] = int(matrix[0][i])
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    res = max(res, dp[i][j])
        return res**2

