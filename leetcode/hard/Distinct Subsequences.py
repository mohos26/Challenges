# https://leetcode.com/problems/distinct-subsequences/
# 28.04.2026


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def dfs(i, j):
            if i == len(s) or j == len(t) or len(t) - j > len(s) - i:
                return int(j == len(t))
            key = i, j
            if key not in memo:
                memo[key] = (s[i] == t[j]) * dfs(i+1, j+1) + dfs(i+1, j)
            return memo[key]
        return dfs(0, 0)

