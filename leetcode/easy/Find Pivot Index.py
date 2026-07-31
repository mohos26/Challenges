# https://leetcode.com/problems/find-pivot-index/
# 31.07.2026


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = [], []
        for i, j in zip(range(len(nums)), range(len(nums)-1, -1, -1)):
            if i == 0:
                left.append(nums[i])
                right.append(nums[j])
            else:
                left.append(left[-1] + nums[i])
                right.append(right[-1] + nums[j])
        right.reverse()
        for i, a, b in zip(range(len(nums)), left, right):
            if a == b:
                return i
        return -1

