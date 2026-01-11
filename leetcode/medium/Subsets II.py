# https://leetcode.com/problems/subsets-ii
# 08.01.2026


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def dfs(lst, i):
            if i == len(nums):
                res.add(tuple(sorted(lst)))
                return
            lst.append(nums[i])
            dfs(lst, i+1)
            lst.pop()
            dfs(lst, i+1)
        dfs([], 0)
        return list(res)


class Solution_2:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(lst, i):
            if i == len(nums):
                res.append(lst.copy())
                return
            lst.append(nums[i])
            dfs(lst, i+1)
            lst.pop()
            for j in range(i+1, len(nums)):
                if nums[i] != nums[j]:
                    i = j - 1
                    break
            else:
                i = len(nums) - 1
            dfs(lst, i+1)
        dfs([], 0)
        return res

