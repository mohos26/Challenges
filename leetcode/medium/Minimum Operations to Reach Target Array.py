# https://leetcode.com/problems/minimum-operations-to-reach-target-array
# 17.01.2026


class Solution:
    def minOperations(self, nums: List[int], target: List[int]) -> int:
        d = defaultdict(list)
        for i, n in enumerate(nums):
            if nums[i] != target[i]:
                d[n].append(i)
        return len(d)

