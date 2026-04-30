# https://leetcode.com/problems/edit-distance/
# 30.04.2026


class Solution:
    def delete(self, word, i):
        return word[:i] + word[i+1:]

    def insert(self, word, letter, i):
        return word[:i] + letter + word[i:]

    def replace(self, word, letter, i):
        return word[:i] + letter + word[i+1:]

    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def dfs(curr, i, j):
            if max(i, j) >= max(len(curr), len(word2)):
                if curr == word2:
                    return 0
                return float("inf")
            key = i, j, curr
            if key not in memo:
                memo[key] = float("inf")
                # insert
                if j < len(word2):
                    memo[key] = min(memo[key], dfs(self.insert(curr, word2[j], i), i+1, j+1)+1)
                # delete
                if i < len(curr):
                    memo[key] = min(memo[key], dfs(self.delete(curr, i), i, j)+1)

                if i < len(curr) and j < len(word2):
                    if curr[i] == word2[j]:
                        memo[key] = min(memo[key], dfs(curr, i+1, j+1)) # nothing
                    else:
                        memo[key] = min(memo[key], dfs(self.replace(curr, word2[j], i), i+1, j+1)+1) # replace
            return memo[key]
        return dfs(word1, 0, 0)

