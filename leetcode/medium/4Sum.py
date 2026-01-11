# https://leetcode.com/problems/4sum
# 14.12.2026


class Solution:
    def threeSum(self, nums: List[int], target, first) -> List[List[int]]:
        res = []
        for i in range(len(nums)-2):
            if i and nums[i] == nums[i-1]:
                continue
            a = nums[i]
            left, right = i+1, len(nums)-1
            while left < right:
                b = nums[left] + nums[right]
                if b == target - a:
                    res.append((first, a, nums[left], nums[right]))
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                elif b > target - a:
                    right -= 1
                else:
                    left += 1
        return res


    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for i, n in enumerate(nums):
            if i and n == nums[i-1]:
                continue
            res.extend(self.threeSum(nums[i+1:], target-n, n))
        return res

