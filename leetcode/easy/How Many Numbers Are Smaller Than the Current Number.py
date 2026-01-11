# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number
# 08.12.2026


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        d = dict(zip(sorted(nums, reverse=True), range(len(nums)-1, -1, -1)))
        for n in nums:
            result.append(d[n])
        return result

