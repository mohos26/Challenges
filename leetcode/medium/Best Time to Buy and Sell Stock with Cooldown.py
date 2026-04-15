# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# 15.04.2026


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, stock, status):
            if i >= len(prices):
                return 0
            key = (i, stock, status)
            if key not in memo:
                if status:
                    memo[key] = max(prices[i] - stock + dfs(i+2, 0, False), dfs(i+1, stock, status))
                else:
                    memo[key] = max(dfs(i+1, prices[i], True), dfs(i+1, 0, False))
            return memo[key]
        return dfs(0, 0, False)

