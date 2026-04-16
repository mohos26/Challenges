# https://leetcode.com/problems/coin-change-ii/
# 16.04.2026


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = defaultdict(int)
        def dfs(i, total):
            if total > amount or i == len(coins):
                return 0
            if total == amount:
                return 1
            key = i, total
            if key not in memo:
                memo[key] = dfs(i, total + coins[i]) + dfs(i+1, total)
            return memo[key]
        return dfs(0, 0)

