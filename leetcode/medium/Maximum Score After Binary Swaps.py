# https://leetcode.com/problems/maximum-score-after-binary-swaps
# 31.12.2025


class Solution:
    def maximumScore(self, nums: List[int], s: str) -> int:
        heap = []
        length = 0
        heap_len = 0
        nums.reverse()
        for a, b in zip(nums, s[::-1]):
            length += int(b)
            heapq.heappush(heap, a)
            heap_len += 1
            if heap_len > length:
                heapq.heappop(heap)
                heap_len -= 1
        return sum(heap)


class Solution_2: # (optimaze)
    def maximumScore(self, nums: List[int], s: str) -> int:
        res = 0
        heap = []
        for a, b in zip(nums, s):
            heapq.heappush(heap, -a)
            if b == '1':
                res -= heapq.heappop(heap)
        return res

