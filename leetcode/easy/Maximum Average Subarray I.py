# https://leetcode.com/problems/maximum-average-subarray-i/
# 26.07.2026


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = None
        curr = 0
        for i, n in enumerate(nums):
            curr += n
            if i >= k - 1:
                res = curr / k if res is None else max(res, curr / k)
                curr -= nums[i-k+1]
        return res

