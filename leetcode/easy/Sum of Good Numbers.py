# https://leetcode.com/problems/sum-of-good-numbers/
# 30.04.2026


class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            a, b = i-k, i+k
            if (0 <= a < n and nums[a] >= nums[i]) or (0 <= b < n and nums[b] >= nums[i]):
                continue
            res += nums[i]
        return res

