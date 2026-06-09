# https://neetcode.io/problems/meeting-schedule/
# 09.06.2026


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted((o.start, o.end) for o in intervals)
        for i in range(1, len(intervals)):
            a, b = intervals[i-1]
            target = intervals[i][0]
            if a <= target < b:
                return False
        return True

