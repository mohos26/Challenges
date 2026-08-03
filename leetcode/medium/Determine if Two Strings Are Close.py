# https://leetcode.com/problems/determine-if-two-strings-are-close
# 03.08.2026


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d1, d2 = Counter(word1), Counter(word2)
        return d1.keys() == d2.keys() and sorted(d1.values()) == sorted(d2.values())

