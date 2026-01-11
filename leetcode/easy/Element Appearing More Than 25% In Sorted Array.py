# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
# 15.10.2026


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        d = Counter(arr)
        length = len(arr)
        for a, b in sorted(d.items(), reverse=True, key=lambda l:l[1]):
            if b * 100 / length >= 25:
                return a
        return -1


# 01.12.2026
class Solution_2:
    def findSpecialInteger(self, arr: List[int]) -> int:
        return max(Counter(arr).items(), key=lambda l:l[1])[0]

