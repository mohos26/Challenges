# https://leetcode.com/problems/maximum-substrings-with-distinct-start/
# 15.01.2026


class Solution:
    def maxDistinct(self, s: str) -> int:
        return len(set(s))

