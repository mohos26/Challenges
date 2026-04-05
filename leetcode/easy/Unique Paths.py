# https://leetcode.com/problems/unique-paths/
# 05.04.2026


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = defaultdict(int)
        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            if not (0 <= i < m and 0 <= j < n):
                return 0
            if (i, j) not in memo:
                memo[(i, j)] = dfs(i, j+1) + dfs(i+1, j)
            return memo[(i, j)]
        return dfs(0, 0)

