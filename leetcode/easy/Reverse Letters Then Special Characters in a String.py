# https://leetcode.com/problems/reverse-letters-then-special-characters-in-a-string/
# 31.01.2026


class Solution:
    def reverseByType(self, s: str) -> str:
        letters = special = ''
        for letter in s[::-1]:
            if letter.isalpha():
                letters += letter
            else:
                special += letter
        res = ''
        i = j = 0
        for letter in s:
            if letter.isalpha():
                res += letters[i]
                i += 1
            else:
                res += special[j]
                j += 1
        return res

