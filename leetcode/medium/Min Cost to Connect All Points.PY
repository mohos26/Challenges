# https://leetcode.com/problems/min-cost-to-connect-all-points
# 22.02.2026


class Solution:
    def manhattan(self, a, b, c, d):
        return abs(a - c) + abs(b - d)

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        points = tuple(map(tuple, points))
        heap = [(0, points[0])]
        visited = set()
        res = 0
        while heap:
            cost, point = heapq.heappop(heap)
            if point in visited:
                continue
            res += cost
            visited.add(point)
            for child in points:
                if child in visited:
                    continue
                heapq.heappush(heap, (self.manhattan(*point, *child), child))
        return res


class Solution:
    def manhattan(self, a, b, c, d):
        return abs(a - c) + abs(b - d)

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = [(0, tuple(points[0]))]
        points = set(map(tuple, points))
        visited = set()
        res = 0
        while heap:
            cost, point = heapq.heappop(heap)
            if point in visited:
                continue
            res += cost
            visited.add(point)
            points.remove(point)
            for child in points:
                heapq.heappush(heap, (self.manhattan(*point, *child), child))
        return res

