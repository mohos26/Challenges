# https://leetcode.com/problems/minimum-removals-to-balance-array/
# 13.06.2026


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        _max = 0
        for i, n in enumerate(nums):
            _max = max(_max, bisect_right(nums, n * k) - i)
        return len(nums) - _max

