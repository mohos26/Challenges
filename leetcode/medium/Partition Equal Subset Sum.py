# https://leetcode.com/problems/partition-equal-subset-sum/
# 03.04.2026


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        _sum = sum(nums)
        if _sum % 2:
            return False
        target = _sum // 2
        memo = defaultdict(bool)
        def dfs(i, n):
            if n == target:
                return True
            if i == len(nums):
                return False
            if (i, n) not in memo:
                memo[(i, n)] = dfs(i+1, n) or dfs(i+1, n + nums[i])
            return memo[(i, n)]
        return dfs(0, 0)

