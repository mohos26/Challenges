# https://leetcode.com/problems/roman-to-integer
# 20.07.25

class Solution:
    d = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }


    def romanToInt(self, s: str) -> int:
        res, last = 0, None
        for letter in s:
            if last and self.d[last] < self.d[letter]:
                res -= 2 * self.d[last]
            res += self.d[letter]
            last = letter
        return res

