# https://leetcode.com/problems/spiral-matrix/
# 20.06.2026


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        i = j = 0
        last = 0
        n, m = len(matrix), len(matrix[0])
        for _ in range(n * m):
            res.append(matrix[i][j])
            matrix[i][j] = None
            base = i, j
            for d in range(4):
                i, j = base
                if last == 0:
                    j += 1
                elif last == 1:
                    i += 1
                elif last == 2:
                    j -= 1
                elif last == 3:
                    i -= 1
                if 0 <= i < n and 0 <= j < m and matrix[i][j] is not None:
                    break
                last = (last + 1) % 4
        return res

