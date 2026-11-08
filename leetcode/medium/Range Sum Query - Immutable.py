# https://leetcode.com/problems/range-sum-query-immutable/
# 08.11.2026


class NumArray:

    def __init__(self, nums: list[int]):
        self.d = {}
        curr = 0
        for i, n in enumerate(nums):
            curr += n
            self.d[i] = curr

    def sumRange(self, left: int, right: int) -> int:
        return self.d[right] - (self.d[left-1] if left > 0 else 0)

