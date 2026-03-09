# https://leetcode.com/problems/decode-ways/
# 09.03.2026


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = defaultdict(int)

        def dfs(i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            if i not in dp:
                dp[i] += dfs(i + 1)
                if i + 1 < len(s) and 0 < int(s[i] + s[i + 1]) <= 26:
                    dp[i] += dfs(i + 2)
            return dp[i]

        return dfs(0)

