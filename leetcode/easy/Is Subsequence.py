# https://leetcode.com/problems/is-subsequence/
# 16.07.2026


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        memo = set()
        def dfs(i, j):
            if i == len(s):
                return True
            key = i, j
            if key not in memo:
                for j in range(j, len(t)):
                    if t[j] == s[i] and dfs(i+1, j+1):
                        return True
                memo.add(key)
            return False
        return dfs(0, 0)


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        dp = [[None] * (m + 1) for _ in range(n + 1)]
        for j in range(m+1):
            dp[0][j] = True
        for i in range(1, n+1):
            dp[i][0] = False
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1]
