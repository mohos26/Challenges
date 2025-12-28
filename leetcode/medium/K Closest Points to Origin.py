# https://leetcode.com/problems/k-closest-points-to-origin/
# 28.12.2025


class Solution: # sort
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda l: sqrt(l[0]**2+l[1]**2))
        return points[:k]



class Solution_2: # heap
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for a, b in points:
            heapq.heappush(heap, [round(sqrt(a**2+b**2), 6), [a, b]])
        return [heapq.heappop(heap)[1] for _ in range(k)]

