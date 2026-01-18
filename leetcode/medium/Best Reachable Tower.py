# https://leetcode.com/problems/best-reachable-tower/
# 17.01.2026


class Solution:
    def ft_aid(self, l1, l2):
        return abs(l1[0] - l2[0]) + abs(l1[1] - l2[1])

    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        res = []
        for x, y, q in towers:
            if not res and self.ft_aid([x, y], center) <= radius:
                res = [x, y, q]
            elif (self.ft_aid([x, y], center) <= radius and q >= res[2]):
                if q == res[2]:
                    res = min(res, [x, y, q])
                else:
                    res = [x, y, q]
        return (res[0], res[1]) if res else [-1, -1]

