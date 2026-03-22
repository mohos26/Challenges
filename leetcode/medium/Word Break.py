# https://leetcode.com/problems/word-break/
# 22.03.2026


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        _set = set()
        def dfs(s):
            if not s:
                return True
            if s in _set:
                return False
            for word in wordDict:
                if s.startswith(word) and dfs(s[len(word):]):
                    return True
            _set.add(s)
            return False
        return dfs(s)

