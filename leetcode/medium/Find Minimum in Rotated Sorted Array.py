# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
# 18.11.25


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            if left == right:
                return nums[left]
            medium = left + (right - left) // 2
            if nums[medium] > nums[right]:
                left = medium + 1
            else:
                right = medium
        return -1

