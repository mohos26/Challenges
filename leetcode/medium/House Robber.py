# https://leetcode.com/problems/house-robber/
# 02.03.2026


class Solution:
    def rob(self, nums: List[int]) -> int:
        d = defaultdict(int)
        def dfs(i):
            if i not in d:
                for j in range(i + 2, len(nums)):
                    d[i] = max(d[i], dfs(j))
                print(i)
                d[i] += nums[i]
            return d[i]
        dfs(0)
        if len(nums) > 1:
            dfs(1)
        return max(d.values())

