# https://leetcode.com/problems/max-consecutive-ones-iii
# 17.01.2026


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        res = 0
        len_ones = 0
        for r in range(len(nums)):
            len_ones += nums[r]
            if r - l - len_ones + 1 <= k:
                res = max(res, r - l + 1)
            else:
                len_ones -= nums[l]
                l += 1
        return res

