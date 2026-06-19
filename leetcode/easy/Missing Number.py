# https://leetcode.com/problems/missing-number/
# 19.06.2026


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        for n in range(0, len(nums)+1):
            res ^= n
        return res

