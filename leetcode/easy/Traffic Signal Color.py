# https://leetcode.com/problems/traffic-signal-color/
# 15.04.2026


class Solution:
    def trafficSignal(self, timer: int) -> str:
        if timer == 0:
            return "Green"
        elif timer == 30:
            return "Orange"
        elif 30 < timer <= 90:
            return "Red"
        return "Invalid"

