# https://neetcode.io/problems/meeting-schedule-ii/
# 09.06.2026


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res = 0
        exp = []
        # 1: open, 0: close
        for o in intervals:
            exp.append((o.start, 1))
            exp.append((o.end, 0))
        exp.sort()
        stack = 0
        for _, stat in exp:
            if stat == 1:
                stack += 1
                if stack > res:
                    res = stack
            else:
                stack -= 1
        return res

