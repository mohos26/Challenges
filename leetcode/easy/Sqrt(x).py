# https://leetcode.com/problems/sqrtx
# 27.12.2025


class Solution:
    def mySqrt(self, x: int) -> int:
        for n in range(1, max(ceil(x / 2) + 1, 3)):
            if n**2 == x:
                return n
            elif n**2 > x:
                return n - 1
        return x

