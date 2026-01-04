# https://leetcode.com/problems/minimum-subarray-length-with-distinct-sum-at-least-k
# 04.01.2025


class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        _sum = 0
        d = defaultdict(int)
        res = float("inf")
        for r in range(len(nums)):
            if not d[nums[r]]:
                _sum += nums[r]
            d[nums[r]] += 1
            if _sum >= k:
                while l < r and _sum - nums[l] * (not d[nums[l]] - 1)>= k:
                    d[nums[l]] -= 1
                    if not d[nums[l]]:
                        _sum -= nums[l]
                    l += 1
                res = min(res, r - l + 1)
        return res if res != float("inf") else -1

