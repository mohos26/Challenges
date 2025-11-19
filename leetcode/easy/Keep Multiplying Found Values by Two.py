# https://leetcode.com/problems/keep-multiplying-found-values-by-two
# 19.11.25


# sort + binary search o(n log n)
class Solution:
    def search(self, target):
        left, right = 0, len(self.nums) - 1
        while left <= right:
            medium = left + (right - left) // 2
            if self.nums[medium] == target:
                return True
            elif self.nums[medium] > target:
                right = medium - 1
            else:
                left = medium + 1
        return False

    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        self.nums = nums
        while self.search(original):
            original *= 2
        return original


# hash_table o(n)
class Solution_2:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        hash_table = set(nums)
        while original in hash_table:
            original *= 2
        return original

# sorting + linear search o(n log n)
class Solution_3:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        for n in nums:
            if n == original:
                original *= 2
        return original

