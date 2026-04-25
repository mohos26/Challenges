# https://leetcode.com/problems/interleaving-string/
# 25.04.2026


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        memo = set()
        def dfs(s1, s2, i):
            if i == len(s3):
                return True
            key = i, s1, s2
            if key not in memo:
                if s1 and s1[0] == s3[i] and dfs(s1[1:], s2, i+1):
                    return True
                if s2 and s2[0] == s3[i] and dfs(s1, s2[1:], i+1):
                    return True
                memo.add(key)
            return False
        return dfs(s1, s2, 0)

