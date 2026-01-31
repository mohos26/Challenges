# https://leetcode.com/problems/minimum-k-to-reduce-array-within-limit/
# 31.01.2026


class Solution:
    def nonPositive(self, nums, k):
        res = 0
        for n in nums:
            res += ceil(n / k)
        return res

    def minimumK(self, nums: List[int]) -> int:
        left, right = 1, max(max(nums),len(nums))
        while left < right:
            mid = left + (right - left) // 2
            if self.nonPositive(nums, mid) <= mid**2:
                right = mid
            else:
                left = mid + 1
        return left

