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


# 23.02.2026
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


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        min_cost = [float("inf")] * n
        min_cost[0] = 0
        visited = [False] * n
        res = 0
        for _ in range(n):
            curr = -1
            for i in range(n):
                if not visited[i] and (curr == -1 or min_cost[curr] > min_cost[i]):
                    curr = i
            visited[curr] = True
            res += min_cost[curr]
            x1, y1 = points[curr]
            for i in range(n):
                if not visited[i] and curr != i:
                    x2, y2 = points[i]
                    min_cost[i] = min(min_cost[i], abs(x1 - x2) + abs(y1 - y2))
        return res

