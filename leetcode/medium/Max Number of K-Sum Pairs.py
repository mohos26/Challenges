# https://leetcode.com/problems/max-number-of-k-sum-pairs
# 24.07.2026


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        res = 0
        nums.sort()
        left, right = 0, len(nums) - 1
        while left < right:
            target = nums[left] + nums[right]
            if target == k:
                res += 1
                left += 1
                right -= 1
            elif target < k:
                left += 1
            else:
                right -= 1
        return res


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        res = 0
        d = Counter(nums)
        for n in d:
            if n >= k:
                continue
            m = k - n
            if m in d:
                count = min(d[m], d[n])
                if m == n:
                    count //= 2
                d[n] -= count
                d[m] -= count
                res += count
        return res

