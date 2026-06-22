# https://leetcode.com/problems/sum-of-two-integers/
# 22.06.2026


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b & mask:
            a, b = a ^ b, (a & b) << 1
        return (a & mask) if b > 0 else a

