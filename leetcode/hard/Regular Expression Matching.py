# https://leetcode.com/problems/regular-expression-matching
# 20.05.2026


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = s[::-1]
        p = p[::-1]
        memo = set()
        def dfs(i, j):
            if i >= len(s) and j >= len(p):
                return True
            key = i, j
            if key not in memo:
                memo.add(key)
                if (j < len(p) and p[j] == '.') or (j < len(p) and i < len(s) and p[j] == s[i]):
                    return dfs(i+1, j+1)
                elif j < len(p) and p[j] == '*':
                    arg = p[j+1]
                    j += 2
                    if arg == '.':
                        for ii in range(i, len(s)+1):
                            if dfs(ii, j):
                                return True
                    else:
                        while i < len(s) and arg == s[i]:
                            if dfs(i, j):
                                return True
                            i += 1
                        return dfs(i, j)
            return False
        return dfs(0, 0)

