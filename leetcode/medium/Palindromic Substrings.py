# https://leetcode.com/problems/palindromic-substrings
# 08.03.2026


class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        dp = defaultdict(bool)
        for length in range(1, len(s) + 1):
            for i in range(0, len(s)):
                j = i + length - 1
                if j >= len(s):
                    break
                if s[i] == s[j] and (length <= 2 or dp[(i+1, j-1)]):
                    dp[(i, j)] = True
                    res += 1
        return res

