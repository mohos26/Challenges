# https://leetcode.com/problems/minimum-interval-to-include-each-query/
# 10.06.2026


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        i = 0
        heap = []
        intervals.sort()
        res = [0] * len(queries)
        for n, j in sorted((v, i) for i, v in enumerate(queries)):
            while i < len(intervals) and intervals[i][0] <= n:
                heapq.heappush(heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1
            while heap and heap[0][1] < n:
                heapq.heappop(heap)
            res[j] = (heap[0][0] if heap else -1)
        return res

