# https://leetcode.com/problems/minimum-window-substring
# 19.10.2026
# 31.10.2026


class Solution_brute_force:
    def minWindow(self, s: str, t: str) -> str:
        res = None
        t = Counter(t)
        for left in range(len(s)):
            if not t[s[left]]:
                continue
            t_copy = t.copy()
            for right in range(left, len(s)):
                if t_copy[s[right]]:
                    t_copy[s[right]] -= 1
                if not any(t_copy.values()):
                    break
            else:
                break
            if not res or res[1] - res[0] > right - left:
                res = left, right
        if not res:
            return ""
        return s[res[0] : res[1] + 1]


class Solution:
    def checker(self, base, other):
        for key, value in base.items():
            if other[key] < value:
                return False
        return True


    def minWindow(self, s: str, t: str) -> str:
        res = None
        base = Counter(t)
        aid = defaultdict(int)
        right = 0
        for left in range(len(s)):
            if s[left] not in base:
                continue
            right = max(right, left)
            if self.checker(base, aid):
                if not res or right - left < res[1] - res[0]:
                    res = left, right
                aid[s[left]] -= 1
                continue
            while not self.checker(base, aid) and right < len(s):
                aid[s[right]] += 1
                right += 1
            print(left, right)
            if self.checker(base, aid):
                if not res or right - left < res[1] - res[0]:
                    res = left, right
            else:
                break
            aid[s[left]] -= 1
        if res:
            return s[res[0]:res[1]]
        return ""

