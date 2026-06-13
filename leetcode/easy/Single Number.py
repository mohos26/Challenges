# https://leetcode.com/problems/single-number/
# 13.06.2026


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res

