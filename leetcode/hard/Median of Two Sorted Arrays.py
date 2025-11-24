# https://leetcode.com/problems/median-of-two-sorted-arrays/description
# 20.07.25


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst = sorted(nums1 + nums2)
        if len(lst) % 2:
            return lst[len(lst) // 2]
        return (lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) / 2


# 24.11.2025
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        flag = length % 2
        target_length = length // 2 + 1
        while length > target_length:
            if nums1 and nums2:
                if nums1[0] > nums2[0]:
                    nums2.pop(0)
                else:
                    nums1.pop(0)
            elif nums1:
                nums1.pop(0)
            else:
                nums2.pop(0)
            length -= 1
        result = 0
        if flag:
            if nums1 and nums2:
                if nums1[0] > nums2[0]:
                    return nums2[0]
                else:
                    return nums1[0]
            elif nums1:
                return nums1[0]
            return nums2[0]
        for _ in range(2):
            if nums1 and nums2:
                if nums1[0] > nums2[0]:
                    result += nums2.pop(0)
                else:
                    result += nums1.pop(0)
            elif nums1:
                result += nums1.pop(0)
            else:
                result += nums2.pop(0)
        return result / 2

