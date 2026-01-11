# https://leetcode.com/problems/day-of-the-year/
# 05.01.2026


class Solution:
    def dayOfYear(self, date: str) -> int:
        dct = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        y, m, d = map(int, date.split('-'))
        if not y % 400 or (not y % 4 and y % 100):
            dct[2] += 1
        res = d
        for i in range(1, m):
            res += dct[i]
        return res
