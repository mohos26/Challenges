# https://leetcode.com/problems/search-in-rotated-sorted-array
# 18.11.25


# find min
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            if left == right:
                return left
            medium = left + (right - left) // 2
            if nums[medium] > nums[right]:
                left = medium + 1
            else:
                right = medium
        return -1

    def search(self, nums: List[int], target: int) -> int:
        min_v = self.findMin(nums)
        if nums[min_v] <= target <= nums[-1]:
            left, right = min_v, len(nums) - 1
        else:
            left, right = 0, min_v
        while left <= right:
            medium = left + (right - left) // 2
            if nums[medium] == target:
                return medium
            elif nums[medium] > target:
                right = medium - 1
            else:
                left = medium + 1
        return -1


# one pass
class Solution_2:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            medium = left + (right - left) // 2
            print(left, right, medium)
            if nums[medium] == target:
                return medium
            elif nums[left] <= nums[medium]:
                if nums[left] <= target < nums[medium]:
                    right = medium - 1
                else:
                    left = medium + 1
            else:
                if nums[medium] < target <= nums[right]:
                    left = medium + 1
                else:
                    right = medium - 1
        return -1

