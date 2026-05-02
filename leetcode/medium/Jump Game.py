# https://leetcode.com/problems/jump-game/
# 02.05.2026


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        _set = set()
        def dfs(i):
            if i >= len(nums) - 1:
                return True
            if i not in _set:
                _set.add(i)
                if nums[i] == 0:
                    return False
                for j in range(i+nums[i], i, -1):
                    if dfs(j):
                        return True
            return False
        return dfs(0)

