# https://leetcode.com/problems/minimum-absolute-difference-between-two-values/
# 28.03.2026


class Solution: # contest
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        res = float("inf")
        a = b = None
        for i, n in enumerate(nums):
            if n == 1:
                a = i
            elif n == 2:
                b = i
            else:
                continue
            if a is not None and b is not None:
                res = min(res, abs(a-b))
        return res if res != float("inf") else -1

