# https://leetcode.com/problems/smallest-pair-with-different-frequencies/
# 28.02.2026


class Solution: # contest
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        d = Counter(nums)
        keys = sorted(d.keys())
        last = keys[0]
        for key in keys[1:]:
            if d[last] != d[key]:
                return keys[0], key
        return -1, -1

