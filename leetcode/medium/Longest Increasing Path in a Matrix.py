# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# 27.04.2026


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        memo = defaultdict(int)
        def dfs(i, j):
            key = i, j
            if key not in memo:
                lst = []
                memo[key] = 1
                for a, b in ((i-1, j), (i+1, j), (i, j+1), (i, j-1)):
                    if 0 <= a < m and 0 <= b < n:
                        if matrix[a][b] > matrix[i][j]:
                            memo[key] = max(memo[key], dfs(a, b) + 1)
            return memo[key]
        for i in range(m):
            for j in range(n):
                dfs(i, j)
        return max(memo.values())

