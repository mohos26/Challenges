# https://leetcode.com/problems/longest-palindromic-substring/
# 20.07.2025


class Solution:
    def ft_is_palindrome(self, s):
        length = len(s)
        if length % 2:
            return s[:length // 2] == s[length // 2 + 1:][::-1]
        return s[:length // 2] == s[length // 2:][::-1]


    def longestPalindrome(self, s: str) -> str:
        res = []
        for c in set(s):
            if s.count(c) > 1:
                lst, tmp = [], s
                for _ in range(s.count(c)):
                    lst.append(tmp.index(c))
                    tmp = tmp.replace(c, '\0', 1)
                for a, b in combinations(lst, 2):
                    if self.ft_is_palindrome(s[a:b + 1]):
                        res.append(s[a:b + 1])
        if not res:
            return s[0]
        return max(res, key=len)


# 07.03.2026
class Solution:
    def ft_aid(self, s, l, r):
        res = ''
        while 0 <= l <= r < len(s):
            if s[l] != s[r]:
                break
            if r - l + 1 > len(res):
                res = s[l:r+1]
            r += 1
            l -= 1
        return res

    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            res = max(res, self.ft_aid(s, i, i), self.ft_aid(s, i, i+1), key=len)
        return res


class Solution:
    def longestPalindrome(self, s):
        res = ''
        d = defaultdict(bool)
        for length in range(1, len(s) + 1):
            for i in range(len(s)):
                j = i + length - 1
                if j >= len(s):
                    break
                if s[i] == s[j] and (length <= 2 or d[(i+1, j-1)]):
                    d[(i, j)] = True
                    if length > len(res):
                        res = s[i:j+1]
        return res

