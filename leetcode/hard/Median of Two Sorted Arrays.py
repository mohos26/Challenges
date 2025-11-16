# https://leetcode.com/problems/median-of-two-sorted-arrays/description
# 20.07.25


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst = sorted(nums1 + nums2)
        if len(lst) % 2:
            return lst[len(lst) // 2]
        return (lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) / 2

