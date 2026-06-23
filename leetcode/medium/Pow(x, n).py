# https://leetcode.com/problems/powx-n/
# 23.06.2026


class Solution:
    def myPow(self, x: float, n: int) -> float:
        sing = -1 if x < 0 else 1
        x = abs(x)
        base = x
        last = x
        for _ in range(abs(n) - 1):
            x *= base
            if x == last:
                break
            last = x
        if n % 2:
            x *= sing
        if n > 0:
            return x
        elif n == 0:
            return 1
        return 1/x

