# https://leetcode.com/problems/longest-even-odd-subarray-with-threshold
# 25.12.2025


class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        i = 0
        res = 0
        length = len(nums)
        while i < length:
            if nums[i] % 2:
                i += 1
                continue
            aid = 0
            last = 1
            while i < length and nums[i] <= threshold and nums[i] % 2 != last:
                aid += 1
                last = not last
                i += 1
            res = max(res, aid)
            if not aid:
                i += 1
        return res

