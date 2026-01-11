# 27.12.2026
# https://leetcode.com/problems/longest-common-prefix


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        for arg in zip(*strs):
            if len(set(arg)) != 1:
                break
            res += arg[0]
        return res

