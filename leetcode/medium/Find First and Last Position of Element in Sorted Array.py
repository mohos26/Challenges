# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array
# 10.12.2026


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)
        while left < right:
            medium = left + (right - left) // 2
            if nums[medium] == target:
                start = medium
                while True:
                    if start < 0:
                        start += 1
                        break
                    elif nums[start] == target:
                        start -= 1
                    else:
                        start += 1
                        break
                end = medium
                while True:
                    if end == len(nums):
                        end -= 1
                        break
                    elif nums[end] == target:
                        end += 1
                    else:
                        end -= 1
                        break
                return [start, end]
            elif nums[medium] > target:
                right = medium
            else:
                left = medium + 1
        return [-1, -1]

