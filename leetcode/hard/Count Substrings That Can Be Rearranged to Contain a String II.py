# https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-ii/
# 16.01.2026


class Solution:
    def validSubstringCount(self, s: str, t: str) -> int:
        base = Counter(t)
        curr = defaultdict(int)
        curr_len = 0
        base_len = len(t)
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] not in base:
                continue
            curr[s[r]] += 1
            if base[s[r]] >= curr[s[r]]:
                curr_len += 1
            while base_len == curr_len:
                res += len(s) - r
                if s[l] not in base:
                    l += 1
                    continue
                curr[s[l]] -= 1
                if curr[s[l]] < base[s[l]]:
                    curr_len -= 1
                l += 1
        return res

