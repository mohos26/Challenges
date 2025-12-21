# https://leetcode.com/problems/non-overlapping-intervals
# 21.12.2025


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        i = 0
        res = 0
        intervals.sort(key=lambda l: l[1])
        length = len(intervals)
        while i < length:
            min_end = intervals[i][1]
            while i < length:
                if intervals[i][0] >= min_end:
                    break
                i += 1
            res += 1
        return length - res

