# https://leetcode.com/problems/first-unique-even-element/
# 15.03.2026


class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        d = Counter(nums)
        for n in nums:
            if n % 2 == 0 and d[n] == 1:
                return n
        return -1

