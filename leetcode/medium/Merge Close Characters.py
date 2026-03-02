# https://leetcode.com/problems/merge-close-characters/
# 28.02.2026


class Solution: # contest
    def mergeCharacters(self, s: str, k: int) -> str:
        i = 0
        window = {}
        while i < len(s):
            if s[i] in window:
                if i - window[s[i]] <= k:
                    s = s[:i] + s[i+1:]
                else:
                    window[s[i]] = i
                    i += 1
            else:
                window[s[i]] = i
                i += 1
        return s
