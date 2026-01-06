# https://leetcode.com/problems/subsets/
# 05.0.2026


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            tmp = copy.deepcopy(res)
            res.clear()
            for arg in tmp:
                res.append(arg)
                res.append(arg + [n])
            tmp.clear()
        return res


class Solution_2: # recursion
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(lst, i):
            if i == len(nums):
                res.append(lst)
                return
            dfs(lst, i+1)
            dfs(lst + [nums[i]], i+1)
        dfs([], 0)
        return res

