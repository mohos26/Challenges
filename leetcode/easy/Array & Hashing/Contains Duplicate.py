# https://leetcode.com/problems/contains-duplicate
# 09.09.2025
# 18.10.2025


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for n in nums:
            if n in s:
                return True
            s.add(n)
        return False

