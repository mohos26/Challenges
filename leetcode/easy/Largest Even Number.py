# https://leetcode.com/problems/largest-even-number/
# 19.01.2026


class Solution:
    def largestEven(self, s: str) -> str:
        while s and s[-1] == '1':
            s = s[:-1]
        return s

