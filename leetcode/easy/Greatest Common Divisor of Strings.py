# https://leetcode.com/problems/greatest-common-divisor-of-strings/
# 08.07.2026


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = curr = ''
        _min, _max = (str1, str2) if len(str1) < len(str2) else (str2, str1)
        for letter in _min:
            curr += letter
            if len(_max) % len(curr) == 0 \
                and curr * (len(_max) // len(curr)) == _max \
                and curr * (len(_min) // len(curr)) == _min:
                res = curr
        return res

