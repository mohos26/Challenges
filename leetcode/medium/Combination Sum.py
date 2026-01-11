# https://leetcode.com/problems/combination-sum
# 06.01.2026


class Solution_1:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        def dfs(lst):
            if sum(lst) >= target:
                if sum(lst) == target:
                    lst.sort()
                    res.add(tuple(lst))
                return
            for n in candidates:
                dfs(lst + [n])
        dfs([])
        return list(res)


class Solution_2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        def dfs(lst, _sum):
            if _sum >= target:
                if _sum == target:
                    res.add(tuple(sorted(lst)))
                return
            for n in candidates:
                lst.append(n)
                dfs(lst, _sum + n)
                lst.pop()
        dfs([], 0)
        return list(res)


class Solution_3:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(start, lst, _sum):
            if _sum >= target:
                if _sum == target:
                    res.append(lst.copy())
                return
            for i in range(start, len(candidates)):
                lst.append(candidates[i])
                dfs(i, lst, _sum + candidates[i])
                lst.pop()
        dfs(0, [], 0)
        return res

