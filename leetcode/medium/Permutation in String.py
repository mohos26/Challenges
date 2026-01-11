# https://leetcode.com/problems/permutation-in-string/
# 18.10.2026


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        d = Counter(s1)
        aid = Counter(s2[:k])
        if d == aid:
            return True
        for i in range(len(s2) - k):
            aid[s2[i]] -= 1
            aid[s2[i+k]] += 1
            if d == aid:
                return True
        return False

