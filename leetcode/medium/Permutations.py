# https://leetcode.com/problems/permutations
# 06.01.2025


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(lst, base):
            if all(arg is None for arg in base):
                res.append(lst.copy())
                return
            for i in range(len(base)):
                if base[i] is None:
                    continue
                tmp, base[i] = base[i], None
                lst.append(tmp)
                dfs(lst, base)
                lst.pop()
                base[i] = tmp
        dfs([], nums)
        return res

