# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k
# 04.01.2025


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l = 0
        d = Counter(nums[:k])
        length = len(d)
        _sum = sum(d)
        res = _sum if length == k else 0
        for r in range(k, len(nums)):
            d[nums[r]] += 1
            if d[nums[r]] == 1:
                _sum += nums[r]
                length += 1
            d[nums[l]] -= 1
            if not d[nums[l]]:
                length -= 1
                _sum -= nums[l]
            if length == k:
                res = max(res, _sum)
            l += 1
        return res

