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

