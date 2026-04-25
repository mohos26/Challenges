# https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/
# 25.04.2026


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        _set = set(nums)
        if 0 in _set:
            _set.remove(0)
        return len(_set)

