# https://leetcode.com/problems/sort-colors/
# 27.03.2026


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        d = Counter(nums)
        nums[:] = d[0] * [0] + d[1] * [1] + d[2] * [2]


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(1, len(nums)):
            if nums[i] >= nums[i-1]:
                continue
            while i and nums[i] < nums[i-1]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
                i -= 1


# 16.07.2026
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        target, size = 2, len(nums)
        for _ in range(2):
            slow = 0
            for fast in range(size):
                if nums[fast] != target:
                    if nums[slow] == target:
                        nums[slow], nums[fast] = nums[fast], nums[slow]
                    slow += 1
            target, size = 1, slow

