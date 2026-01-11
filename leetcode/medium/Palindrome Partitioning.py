# https://leetcode.com/problems/palindrome-partitioning
# 11.01.2026


class Solution:
    def is_palindrome(self, lst):
        for i in range(len(lst)//2):
            if lst[i] != lst[-i-1]:
                return False
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(lst, i):
            if i == len(s):
                if self.is_palindrome(lst[-1]):
                    res.append([''.join(arg) for arg in lst])
                return
            lst[-1].append(s[i])
            dfs(lst, i + 1)
            lst[-1].pop()
            if self.is_palindrome(lst[-1]):
                lst.append([s[i]])
                dfs(lst, i + 1)
                lst.pop()
        dfs([[s[0]]], 1)
        return res


class Solution_2:
    def is_palindrome(self, s):
        if s[0] != s[-1]:
            return False
        for i in range(len(s) // 2):
            if s[i] != s[-i - 1]:
                return False
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(lst, i):
            if i == len(s):
                if self.is_palindrome(lst[-1]):
                    res.append([arg for arg in lst])
                return
            lst[-1] += s[i]
            dfs(lst, i + 1)
            lst[-1] = lst[-1][:-1]
            if self.is_palindrome(lst[-1]):
                lst.append(s[i])
                dfs(lst, i + 1)
                lst.pop()

        dfs([s[0]], 1)
        return res

