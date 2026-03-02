# https://leetcode.com/problems/min-cost-climbing-stairs/
# 02.03.2026


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        d = {}
        def dfs(i):
            if i >= len(cost):
                return 0
            if i not in d:
                left = dfs(i+1)
                right = dfs(i+2)
                d[i] = min(left, right) + cost[i]
            return d[i]
        return min(dfs(0), dfs(1))

