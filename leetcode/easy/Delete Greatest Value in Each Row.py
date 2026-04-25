# https://leetcode.com/problems/delete-greatest-value-in-each-row/
# 25.04.2026


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        heaps = [[-n for n in grid[i]] for i in range(len(grid))]
        for i in range(len(grid)):
            heapq.heapify(heaps[i])
        res = 0
        for _ in range(len(grid[0])):
            res += max(-heapq.heappop(heaps[i]) for i in range(len(grid)))
        return res

