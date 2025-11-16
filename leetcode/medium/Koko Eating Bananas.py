# https://leetcode.com/problems/koko-eating-bananas
# 16.11.25


class Solution:
    def hours_needed(self, n):
        result = 0
        for a in self.piles:
            result += ceil(a / n)
        return result

    def search(self, right, target):
        left = 1
        result = right
        while left <= right:
            medium = left + (right - left) // 2
            if self.hours_needed(medium) <= target:
                result = medium
                right = medium - 1
            else:
                left = medium + 1
        return result

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        self.piles = piles
        return self.search(max(piles), h)

