# https://leetcode.com/problems/combination-sum-ii
# 06.01.2025


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(start, lst, _sum):
            if _sum >= target:
                if _sum == target:
                    res.append(lst.copy())
                return
            last = None
            for i in range(start, len(candidates)):
                if last == candidates[i]:
                    continue
                if _sum + candidates[i] > target:
                    break
                lst.append(candidates[i])
                dfs(i + 1, lst, _sum + candidates[i])
                lst.pop()
                last = candidates[i]
        dfs(0, [], 0)
        return res

