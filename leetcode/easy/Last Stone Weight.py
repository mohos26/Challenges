# https://leetcode.com/problems/last-stone-weight
# 26.12.2026


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        length = len(stones)
        heap = [-n for n in stones]
        heapq.heapify(heap)
        while length > 1:
            a, b = heapq.heappop(heap), heapq.heappop(heap)
            length -= 2
            if a != b:
                heapq.heappush(heap, a - b)
                length += 1
        return -heap[0] if length else 0

