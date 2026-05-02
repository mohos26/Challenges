# https://leetcode.com/problems/longest-repeating-character-replacement/
# 09.11.2025


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = end = 0
        d = defaultdict(int)
        for start in range(len(s)):
            while not d or end - start - max(d.values()) <= k:
                if end >= len(s):
                    end += 1
                    break
                d[s[end]] += 1
                end += 1
            res = max(res, end - start - 1)
            d[s[start]] -= 1
            if end >= len(s):
                break
        return res


# 02.05.2026
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        window = defaultdict(int)
        for r in range(len(s)):
            window[s[r]] += 1
            if r - l - max(window.values()) + 1 <= k:
                res = max(res, r - l + 1)
            else:
                window[s[l]] -= 1
                l += 1
        return res

