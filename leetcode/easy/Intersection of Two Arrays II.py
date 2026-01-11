# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# 28.12.2026


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        l1 = Counter(nums1)
        nums2.sort()
        last = None
        counter = 0
        for n in nums2:
            if last == n:
                counter += 1
            else:
                if counter and last in l1:
                    res.extend([last]*min(counter, l1[last]))
                counter = 1
            last = n
        if last in l1:
            res.extend([last]*min(counter, l1[last]))
        return res

