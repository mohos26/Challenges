# https://leetcode.com/problems/n-repeated-element-in-size-2n-array
# 02.12.2025


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            if n in s:
                return n
            s.add(n)
        return -1

