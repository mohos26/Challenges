# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
# 08.07.2026


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        _max = max(candies)
        for n in candies:
            res.append(n + extraCandies >= _max)
        return res

