# https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/
# 13.06.2026


class Solution:
    def checkString(self, s: str) -> bool:
        if 'a' in s and 'b' in s:
            return s.rindex('a') < s.index('b')
        return True
