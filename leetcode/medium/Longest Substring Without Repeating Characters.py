# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 20.07.2026


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        lst = [""]
        while i < len(s):
            if s[i] in lst[-1]:
                i -= len(lst[-1]) - 1
                lst.append(s[i])
            else:
                lst[-1] += s[i]
            i += 1
        return max(map(len, lst))


# 30.09.2025
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = bool(s) * 1
        left, right = 0, 1
        while right < len(s):
            if s[right] in s[left:right]:
                left = left + s[left:right].index(s[right]) + 1
            else:
                res = max(res, right - left + 1)
            right += 1
        return res


# 13.10.2025
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        res = 0
        start = 0
        for end, c in enumerate(s):
            if c in d:
                start = max(start, d[c] + 1)
            d[c] = end
            res = max(res, end - start + 1)
        return res


# 28.04.2026
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        window = defaultdict(int)
        for right in range(len(s)):
            rc = s[right]
            window[rc] += 1
            if len(window) == right - left + 1:
                res += 1
            else:
                lc = s[left]
                window[lc] -= 1
                if window[lc] == 0:
                    window.pop(lc)
                left += 1
        return res

