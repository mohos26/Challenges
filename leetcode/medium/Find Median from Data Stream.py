# https://leetcode.com/problems/find-median-from-data-stream
# 04.01.2025


class MedianFinder:
    def __init__(self):
        self.lst = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.lst, num)

    def findMedian(self) -> float:
        length = len(self.lst)
        if length % 2:
            return self.lst[length // 2]
        return (self.lst[length // 2] + self.lst[length // 2 - 1]) / 2

