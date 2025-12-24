# https://leetcode.com/problems/kth-largest-element-in-a-stream
# 24.12.2025


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.lst = sorted(nums)

    def add(self, val: int) -> int:
        bisect.insort(self.lst, val)
        return self.lst[-self.k]

