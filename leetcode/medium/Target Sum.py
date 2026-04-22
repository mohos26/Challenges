# https://leetcode.com/problems/target-sum/
# 22.04.2026


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i, total):
            if i == len(nums):
                return total == target
            key = (i, total)
            if key not in memo:
                memo[key] = dfs(i+1, total + nums[i]) + dfs(i+1, total - nums[i])
            return memo[key]
        return dfs(0, 0)

