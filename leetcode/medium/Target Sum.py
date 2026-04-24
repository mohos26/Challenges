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


# 24.04.2026
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)

        if abs(target) > total_sum:
            return 0

        offset = total_sum
        dp = [[0] * (2 * total_sum + 1) for _ in range(len(nums) + 1)]
        dp[len(nums)][target + offset] = 1
        for i in range(len(nums)-1, -1, -1):
            for j in range(-total_sum, total_sum + 1):
                res = 0
                if j + nums[i] <= total_sum:
                    res += dp[i+1][nums[i] + j + offset]
                if j - nums[i] >= -total_sum:
                    res += dp[i+1][j - nums[i] + offset]
                dp[i][j + offset] = res
        return dp[0][offset]


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]
        dp[0][0] = 1
        for i in range(len(nums)):
            for total, count in dp[i].items():
                dp[i+1][total + nums[i]] += count
                dp[i+1][total - nums[i]] += count
        return dp[len(nums)][target]

