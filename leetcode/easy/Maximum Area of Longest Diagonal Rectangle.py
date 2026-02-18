# https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/
# 17.02.2026


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        d = defaultdict(list)
        for l, L in dimensions:
            d[l**2+L**2].append(l*L)
        return max(d[max(d)])

