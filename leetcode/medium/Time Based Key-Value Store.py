# https://leetcode.com/problems/time-based-key-value-store
# 23.11.2025


class TimeMap:
    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.d:
            self.d[key].append([timestamp, value])
        else:
            self.d[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        lst = self.d[key]
        left, right = 0, len(lst) - 1
        while left <= right:
            medium = left + (right - left) // 2
            if medium == left:
                if lst[right][0] <= timestamp:
                    return lst[right][1]
                if lst[left][0] <= timestamp:
                    return lst[left][1]
                break
            elif lst[medium][0] <= timestamp:
                left = medium
            else:
                right = medium - 1
        return ""

