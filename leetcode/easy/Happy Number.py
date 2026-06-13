# https://leetcode.com/problems/happy-number/
# 12.06.2026


class Solution:
    def isHappy(self, n: int) -> bool:
        _set = set()
        while n not in _set and n != 1:
            _set.add(n)
            n = sum(v*v for v in map(int,str(n)))
        return n == 1

