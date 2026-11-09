# https://leetcode.com/problems/subarray-sum-equals-k/
# 09.11.2026


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefix = defaultdict(int)
        prefix[0] = 1
        curr = 0
        for n in nums:
            curr += n
            res += prefix[curr-k]
            prefix[curr] += 1
        return res

