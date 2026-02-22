# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/
# 21.02.2026


class Solution: # contest
    def minOperations(self, nums: List[int], k: int) -> int:
        aid = nums[0]
        for n in nums[1:]:
            aid ^= n
        bin1, bin2 = bin(aid)[2:], bin(k)[2:]
        _max = max(len(bin1), len(bin2))
        res = 0
        for a, b in zip(bin1.zfill(_max), bin2.zfill(_max)):
            if a != b:
                res += 1
        return res

