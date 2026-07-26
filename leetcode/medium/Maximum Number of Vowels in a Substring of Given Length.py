# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
# 26.07.2026


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = curr = 0
        vowel = "aeiou"
        for i, letter in enumerate(s):
            curr += letter in vowel
            if i >= k - 1:
                res = max(res, curr)
                curr -= s[i-k+1] in vowel
        return res

