# https://leetcode.com/problems/coin-change/
# 17.03.2026


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {amount: 0}
        def dfs(n):
            if n in dp:
                return dp[n]
            elif n > amount:
                return float("inf")
            dp[n] = float("inf")
            for coin in coins:
                dp[n] = min(dp[n], dfs(n + coin) + 1)
            return dp[n]        
        return -1 if dfs(0) == float("inf") else dp[0]

