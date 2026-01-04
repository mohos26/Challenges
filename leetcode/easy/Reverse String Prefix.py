# https://leetcode.com/problems/reverse-string-prefix
# 04.01.2025


class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        return s[:k][::-1] + s[k:]

