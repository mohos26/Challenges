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


# 26.07.2026
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = left = zeros = 0
        for right in range(len(nums)):
            zeros += nums[right] == 0
            if zeros > k:
                zeros -= nums[left] == 0
                left += 1
            else:
                res = max(res, right - left + 1)
        return res

