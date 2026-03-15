# https://leetcode.com/problems/minimum-cost-to-equalize-arrays-using-swaps
# 15.03.2026


class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        res = 0
        d1 = Counter(nums1)
        d2 = Counter(nums2)
        total = Counter(nums1 + nums2)
        for key in total:
            if total[key] % 2:
                return -1
            res += total[key]//2 - min(d1[key], d2[key])
        return res // 2

