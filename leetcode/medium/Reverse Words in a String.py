# https://leetcode.com/problems/reverse-words-in-a-string
# 15.12.2026


class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split()
        lst.reverse()
        return ' '.join(lst)

