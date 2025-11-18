# https://leetcode.com/problems/next-greater-element-i
# 18.11.25

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums1)
        d = dict([(n, i) for i, n in enumerate(nums1)])
        for n in nums2:
            while stack and stack[-1] < n:
                aid = stack.pop()
                if aid in d:
                    res[d[aid]] = n
                    d.pop(aid)
            stack.append(n)
        return res

