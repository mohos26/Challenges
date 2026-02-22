# https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/
# 21.02.2026

class Solution: # contest
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        a = 0
        for letter in firstWord:
            a *= 10
            a += ord(letter) - ord('a')
        b = 0
        for letter in secondWord:
            b *= 10
            b += ord(letter) - ord('a')
        c = 0
        for letter in targetWord:
            c *= 10
            c += ord(letter) - ord('a')
        return a + b == c


class Solution:
    def converting(self, word):
        res = 0
        for letter in word:
            res = res * 10 + ord(letter) - ord('a')
        return res

    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return self.converting(firstWord) + self.converting(secondWord) == self.converting(targetWord)

