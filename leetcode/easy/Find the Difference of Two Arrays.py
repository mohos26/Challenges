# https://leetcode.com/problems/find-the-difference-of-two-arrays/
# 01.08.2026


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = [[], []]
        set1, set2 = map(set, (nums1, nums2))
        for n in set1:
            if n not in set2:
                res[0].append(n)
        for n in set2:
            if n not in set1:
                res[1].append(n)
        return res

