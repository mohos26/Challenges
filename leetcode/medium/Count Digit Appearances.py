# https://leetcode.com/problems/count-digit-appearances/
# 11.04.2026


class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        res = ''.join(map(str, nums))
        return res.count(str(digit))

