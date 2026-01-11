# https://leetcode.com/problems/maximum-sum-of-three-numbers-divisible-by-three
# 21.12.2026


class Solution: # Contest O(n log n)
    def maximumSum(self, nums: List[int]) -> int:
        d = {0:[],1:[],2:[]}
        nums.sort()
        for n in nums:
            d[n%3].append(n)
        res = 0
        if len(d[0]) > 2:
            res = d[0][-3] + d[0][-2] + d[0][-1]
        if len(d[1]) > 2:
            res = max(res, d[1][-3] + d[1][-2] + d[1][-1])
        if len(d[2]) > 2:
            res = max(res, d[2][-3] + d[2][-2] + d[2][-1])
        if len(d[0]) > 0 and len(d[1]) > 0 and len(d[2]) > 0:
            res = max(res, d[2][-1] + d[0][-1] + d[1][-1])
        return res


class Solution_2: # O(n)
    def maximumSum(self, nums: List[int]) -> int:
        lst = [[] for _ in range(3)]
        for n in nums:
            idx = n%3
            if len(lst[idx]) < 3:
                lst[idx].append(n)
            elif n > min(lst[idx]):
                lst[idx].remove(min(lst[idx]))
                lst[idx].append(n)
        res = 0
        if len(lst[0]) == 3:
            res = sum(lst[0])
        if len(lst[1]) == 3:
            res = max(res, sum(lst[1]))
        if len(lst[2]) == 3:
            res = max(res, sum(lst[2]))
        if all(lst):
            res = max(res, max(lst[0]) + max(lst[1]) + max(lst[2]))
        return res

