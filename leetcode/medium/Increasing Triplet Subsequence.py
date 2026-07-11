# https://leetcode.com/problems/increasing-triplet-subsequence/
# 11.07.2026


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1 = min2 = float("inf")
        for n in nums:
            if min1 >= n:
                min1 = n
            elif min2 >= n:
                min2 = n
            else:
                return True
        return False

