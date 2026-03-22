# https://leetcode.com/problems/longest-increasing-subsequence/
# 22.03.2026


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        d = defaultdict(int)
        for i in range(N-1, -1, -1):
            n = nums[i]
            for j in range(i+1, N):
                if nums[j] > n:
                    d[n] = max(d[n], d[nums[j]] + 1)
        if d:
            return max(d.values()) + 1
        return 1

