# https://leetcode.com/problems/minimum-energy-to-maintain-brightness
# 06.06.2026


class Solution:
    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
        res = 0
        target = 0
        if brightness:
            target = ceil(brightness / 3)

        interval = []
        # 0: open, 1: close
        for a, b in intervals:
            interval.append((a, 0))
            interval.append((b, 1))
        interval.sort()

        aid = []
        stack = []
        for point, stat in interval:
            if stat == 0:
                stack.append(point)
            else:
                arg = stack.pop()
                if not stack:
                    aid.append([arg, point])

        for a, b in aid:
            res += (b - a + 1) * target
        return res

