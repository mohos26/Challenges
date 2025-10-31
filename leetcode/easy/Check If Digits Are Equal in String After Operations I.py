# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i
# 31.10.2025

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) != 2:
            aid = ''
            last = int(s[0])
            for n in map(int, s[1:]):
                aid += str((last + n) % 10)
                last = n
            s = aid
            print(s)
        return s[0] == s[1]

