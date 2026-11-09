# https://leetcode.com/problems/find-pivot-index/
# 09.11.2026


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        d = {}
        curr = 0
        for i, n in enumerate(nums):
            curr += n
            d[i] = curr
        lenght = len(nums)
        for i in range(lenght):
            left = (d[i-1] if i > 0 else 0)
            right = d[lenght-1] - d[i]
            if left == right:
                return i
        return -1

