# https://leetcode.com/problems/house-robber-ii/
# 07.03.2026


class Solution:
    def rob(self, nums: List[int]) -> int:
        memoize = defaultdict(int)
        def dfs(i):
            if i >= len(nums):
                return 0
            if i not in memoize:
                memoize[i] = max(dfs(i+2), dfs(i+3)) + nums[i]
            return memoize[i]

        last = nums.pop()
        if nums:
            dfs(0)
        else:
            memoize[0] = last
        nums.append(last)

        tmp = memoize[0]
        memoize.clear()
        memoize[0] = tmp

        return max(memoize[0], dfs(1), dfs(2))

