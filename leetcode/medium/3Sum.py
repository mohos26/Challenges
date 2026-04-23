# https://leetcode.com/problems/3sum
# 13.12.2025


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i and nums[i] == nums[i-1]:
                continue
            a = nums[i]
            left, right = i+1, len(nums)-1
            while left < right:
                b = nums[left] + nums[right]
                if b == -a:
                    res.append([a, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                elif b > -a:
                    right -= 1
                else:
                    left += 1
        return res

# 23.04.2026
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i and nums[i] == nums[i-1]:
                continue
            n = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if n + nums[left] + nums[right] == 0:
                    res.append((n, nums[left], nums[right]))
                if n + nums[left] + nums[right] > 0:
                    right -= 1
                    while left < right and nums[right+1] == nums[right]:
                        right -= 1
                else:
                    left += 1
                    while left < right and nums[left-1] == nums[left]:
                        left += 1
        return res

