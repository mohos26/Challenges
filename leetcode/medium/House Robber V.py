# https://leetcode.com/problems/house-robber-v/
# 15.02.2026


class Solution: # contest
    def rob(self, nums: List[int], colors: List[int]) -> int:
        lst = []
        res = []
        for i in range(len(colors)):
            if lst and colors[lst[0]] == colors[i]:
                lst.append(i)
            elif not lst:
                if res and colors[res[-1]] == colors[i]:
                    lst.extend([res.pop(), i])
                else:
                    res.append(i)
            else:
                if sum(nums[j] for j in lst[::2]) > sum(nums[j] for j in lst[1::2]):
                    res.extend(lst[::2])
                else:
                    res.extend(lst[1::2])
                lst.clear()
                res.append(i)
        if lst:
            if sum(nums[j] for j in lst[::2]) > sum(nums[j] for j in lst[1::2]):
                res.extend(lst[::2])
            else:
                res.extend(lst[1::2])
        return sum(nums[i] for i in res)

