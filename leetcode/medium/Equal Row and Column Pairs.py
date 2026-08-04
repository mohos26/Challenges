# https://leetcode.com/problems/equal-row-and-column-pairs/
# 04.08.2026


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        res = 0
        n = len(grid)
        row, column = [], []
        for i in range(n):
            row.append(tuple(grid[i]))
            column.append([])
            for j in range(n):
                column[-1].append(grid[j][i])
            column[-1] = tuple(column[-1])
        row, column = Counter(row), Counter(column)
        for key in row:
            if key in column:
                res += row[key] * column[key]
        return res

