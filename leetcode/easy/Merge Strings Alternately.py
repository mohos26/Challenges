# https://leetcode.com/problems/merge-strings-alternately/
# 03.04.2026


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        res = ''
        min_len = min(len(word1), len(word2))
        for i in range(min_len):
            res += word1[i] + word2[i]
        res += word1[min_len:] + word2[min_len:]
        return res

