# https://leetcode.com/problems/maximum-total-value-of-covered-indices/
# 06.06.2026


class Solution:
    def maxTotal(self, nums: List[int], s: str) -> int:
        save = nums.copy()
        for i in range(1, len(nums)):
            if s[i] == '1' and nums[i] < nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
        first = sum(nums[x] for x in range(len(nums)) if s[x] == '1')

        for i in range(len(save) - 1, 0, -1):
            if s[i] == '1' and save[i] < save[i-1]:
                save[i], save[i-1] = save[i-1], save[i]

        second = sum(save[x] for x in range(len(save)) if s[x] == '1')
        return max(first, second)

