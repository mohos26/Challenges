# https://leetcode.com/problems/can-place-flowers
# 10.07.2026


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        lst = []
        start = None
        for i, stat in enumerate(flowerbed):
            if stat == 1 and start is not None:
                lst.append((start, i - 1))
                start = None
            elif stat == 0 and start is None:
                start = i
        if start is not None:
            lst.append((start, len(flowerbed)-1))
        capacity = 0
        for a, b in lst:
            size = b - a
            if a == 0:
                size += 1
            if b == len(flowerbed) - 1:
                size += 1
            capacity += size // 2
        return capacity >= n

