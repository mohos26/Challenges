# https://leetcode.com/problems/reverse-integer/
# 25.06.2026


class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        sing = -1 if x < 0 else 1
        x = abs(x)
        while x:
            res *= 10
            res += x % 10
            x //= 10
        if res > 2**31-1:
            return 0
        return res * sing

