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


class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if not self.max_heap:
            heapq.heappush(self.max_heap, -num)
        elif len(self.min_heap) < len(self.max_heap) or num > self.min_heap[0]:
            if -self.max_heap[0] > num:
                tmp = num
                num = -heapq.heappop(self.max_heap)
                heapq.heappush(self.max_heap, -tmp)
            if len(self.min_heap) == len(self.max_heap):
                heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        return -self.max_heap[0]

