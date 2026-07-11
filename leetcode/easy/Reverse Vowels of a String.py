# https://leetcode.com/problems/reverse-vowels-of-a-string/
# 11.07.2026


class Solution:
    def reverseVowels(self, s: str) -> str:
        lst = []
        target = "aeiouAEIOU"
        for i, letter in enumerate(s):
            if letter in target:
                lst.append((i, letter))
        res = list(s)
        for arg1, arg2 in zip(lst, lst[::-1]):
            res[arg1[0]], res[arg2[0]] = arg2[1], arg1[1]
        return ''.join(res)

