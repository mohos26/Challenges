# https://leetcode.com/problems/valid-palindrome/
# 14.09.2025


class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for letter in s:
            if letter.isalnum():
                res += letter.lower()
        return res == res[::-1]


# 23.04.2026
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()
        return s == s[::-1]

