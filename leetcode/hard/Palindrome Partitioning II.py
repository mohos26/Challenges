# https://leetcode.com/problems/palindrome-partitioning-ii/
# 19.06.2026


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        is_palindrom = [[False] * n for _ in range(n)]
        for l in range(1, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                if s[i] == s[j]:
                    if l <= 2 or is_palindrom[i+1][j-1]:
                        is_palindrom[i][j] = True
        cuts = list(range(n))
        for i in range(n):
            for j in range(i+1):
                if is_palindrom[j][i]:
                    if j == 0:
                        cuts[i] = 0
                        break
                    cuts[i] = min(cuts[i], cuts[j-1]+1)
        return cuts[-1]

