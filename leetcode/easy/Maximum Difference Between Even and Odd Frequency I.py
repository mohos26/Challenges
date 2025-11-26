# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i
# 26.11.2025


class Solution:
    def maxDifference(self, s: str) -> int:
        max_odd, min_even = 0, float("inf")
        for a in Counter(s).values():
            if a % 2:
                max_odd = max(max_odd, a)
            else:
                min_even = min(min_even, a)
        return max_odd - min_even

