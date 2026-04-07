# https://leetcode.com/problems/longest-consecutive-sequence/
# 14.09.2025


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums = set(nums)
        for n in nums:
            if not n - 1 in nums:
                aid = 1
                while n + aid in nums:
                    aid += 1
                res = max(res, aid)
        return res


# 07.04.2026
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        hash_table = set(nums)
        for n in hash_table.copy():
            if n not in hash_table or n - 1 in hash_table:
                continue
            curr = 0
            while n in hash_table:
                hash_table.remove(n)
                curr += 1
                n += 1
            res = max(res, curr)
        return res

