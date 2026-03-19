# https://leetcode.com/problems/maximum-product-subarray/
# 19.03.2026


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        _min = _max = 1
        for n in nums:
            if n == 0:
                _min = _max = 1
                res = max(res, 0)
            else:
                _max, _min = max(_max * n, _min * n, n), min(_max * n, _min * n, n)
                res = max(res, _max)
        return res

