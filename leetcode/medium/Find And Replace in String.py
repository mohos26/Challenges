# https://leetcode.com/problems/find-and-replace-in-string
# 02.01.2026


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        d = {}
        for a, b, c in zip(indices, sources, targets):
            if s.startswith(b, a):
                d[a] = b, c
        for a, b, c in ((i, d[i][0], d[i][1]) for i in sorted(d, reverse=True)):
            if s.startswith(b, a):
                s = s[:a] + c + s[a+len(b):]
        return s


class Solution_2:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        for index, source, target in sorted(zip(indices, sources, targets), reverse=True):
            if s.startswith(source, index):
                s = s[:index] + target + s[index+len(source):]
        return s

