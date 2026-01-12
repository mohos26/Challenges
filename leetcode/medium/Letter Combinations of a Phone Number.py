# https://leetcode.com/problems/letter-combinations-of-a-phone-number
# 12.01.2026


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        d = {'2': "abc", '3': "def", '4': "ghi",
             '5': "jkl", '6': "mno", '7': "pqrs",
             '8': "tuv", '9': "wxyz"}
        def dfs(s, i):
            if i == len(digits):
                res.append(s)
                return
            for letter in d[digits[i]]:
                dfs(s + letter, i + 1)
        dfs('', 0)
        return res

