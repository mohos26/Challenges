# https://leetcode.com/problems/burst-balloons/
# 09.05.2026


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        memo = defaultdict(int)
        nums.insert(0, 1)
        nums.append(1)
        def dfs(l, r):
            if l > r:
                return 0
            key = l, r
            if key not in memo:
                for i in range(l, r+1):
                    aid = nums[l-1] * nums[i] * nums[r+1]
                    memo[key] = max(memo[key], dfs(i+1, r) + aid + dfs(l, i-1))
            return memo[key]
        return dfs(1, len(nums) - 2)

