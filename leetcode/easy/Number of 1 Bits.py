# https://leetcode.com/problems/number-of-1-bits/
# 06.08.2025


class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')


# 14.06.2026
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res

