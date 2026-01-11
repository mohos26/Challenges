# https://leetcode.com/problems/3sum-closest
# 11.01.2026


class Solution:
    def ft_aid(self, a, b, target):
        if a is None:
            return b
        if abs(target - a) > abs(target - b):
            return b
        return a

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = None
        nums.sort()
        for i in range(len(nums)):
            if i and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                res = self.ft_aid(res, nums[left] + nums[right] + nums[i], target)
                if nums[left] + nums[right] + nums[i] == target:
                    return res
                elif nums[left] + nums[right] + nums[i] > target:
                    right -= 1
                else:
                    left += 1
        return res


class Solution_2:
    def ft_aid(self, a, b, target):
        if a is None:
            return b
        if abs(target - a) > abs(target - b):
            return b
        return a

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = None
        nums.sort()
        for i in range(len(nums) - 2):
            min_sum = nums[i] + nums[i+1] + nums[i+2]
            if min_sum > target:
                res =  self.ft_aid(res, min_sum, target)
                break
            max_sum = nums[i] + nums[-2] + nums[-1]
            if max_sum < target:
                res =  self.ft_aid(res, max_sum, target)
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                _sum = nums[left] + nums[right] + nums[i]
                res = self.ft_aid(res, _sum, target)
                if _sum == target:
                    return res
                elif _sum > target:
                    right -= 1
                else:
                    left += 1
        return res

