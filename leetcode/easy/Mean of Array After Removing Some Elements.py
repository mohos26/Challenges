# https://leetcode.com/problems/mean-of-array-after-removing-some-elements/
# 21.02.2026


class Solution: # contest
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        lst = arr[5*len(arr)//100:-5*len(arr)//100]
        return sum(lst) / len(lst)

