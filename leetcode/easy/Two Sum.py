# https://leetcode.com/problems/two-sum
# 20.07.2026
# 09.09.2026


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i+1:]):
                if a + b == target:
                    return [i, j + i + 1]
        return []


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = Counter(nums)
        for n in d:
            if target - n in d.keys():
                if 2 * n == target:
                    if d[n] == 1:
                        continue
                i = nums.index(n)
                j = nums[i+1:].index(target - n) + i + 1
                return [i, j]
        return []

