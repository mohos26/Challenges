# https://leetcode.com/problems/swim-in-rising-water/
# 23.02.2026


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        pq = [(grid[0][0], (0, 0))]
        visited = set()
        while pq:
            cost, point = heapq.heappop(pq)
            if point in visited:
                continue
            visited.add(point)
            x, y = point
            if x == M - 1 and y == N - 1:
                return cost
            for i, j in (x, y+1), (x+1, y), (x, y-1), (x-1, y):
                if not (0 <= i < M and 0 <= j < N):
                    continue
                heapq.heappush(pq, (max(cost, grid[i][j]), (i, j)))
        raise RuntimeError("???")

