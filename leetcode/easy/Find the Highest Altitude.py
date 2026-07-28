# https://leetcode.com/problems/find-the-highest-altitude/
# 28.07.2026


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = curr = 0
        for n in gain:
            curr += n
            res = max(res, curr)
        return res

