# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
# 28.07.2026


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        curr = left = 0
        for right, n in enumerate(nums):
            curr += n
            if right - left + 1 > curr + 1:
                curr -= nums[left]
                left += 1
        return right - left

