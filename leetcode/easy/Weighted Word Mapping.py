# https://leetcode.com/problems/weighted-word-mapping/description/
# 15.02.2026


class Solution: # contest
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = ''
        for word in words:
            aid = 0
            for letter in word:
                aid += weights[ord(letter) - ord('a')]
            aid %= 26
            res += chr(ord('z') - aid)
        return res

