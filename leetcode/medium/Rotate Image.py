# https://leetcode.com/problems/rotate-image/
# 15.06.2026


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        shift = 0
        n = len(matrix)
        for _ in range(n//2):
            for i in range(n-1):
                last = matrix[shift][shift+i]
                for direction in range(4):
                    if direction == 0:
                        aid = n * (i+1) -1
                    elif direction == 1:
                        aid = n**2 - (i+1) // n
                    elif direction == 2:
                        aid = i - (n - 1) * (n**2 - i)
                    elif direction == 3:
                        aid = (n**2 - i) // n - 1
                    a, b = shift + aid // n, shift + aid % n
                    matrix[a][b], last = last, matrix[a][b]
                    i = aid
            shift += 1
            n -= 2

