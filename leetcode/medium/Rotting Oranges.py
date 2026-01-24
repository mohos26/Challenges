# https://leetcode.com/problems/rotting-oranges/
# 22.01.2026

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0
        lst = []
        len_fresh = 0
        N, M = len(grid), len(grid[0])
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    len_fresh += 1
                elif grid[i][j] == 2:
                    lst.append((i, j))
        while len_fresh:
            tmp = []
            res += 1
            for i, j in lst:
                for a, b in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                    if 0 <= a < N and 0 <= b < M and grid[a][b] == 1:
                        grid[a][b] = 2
                        tmp.append((a, b))
                        len_fresh -= 1
            if not tmp:
                return -1
            lst = tmp
        return res


class Solution_2:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0
        lst = deque()
        len_fresh = 0
        N, M = len(grid), len(grid[0])
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    len_fresh += 1
                elif grid[i][j] == 2:
                    lst.append((i, j))
        lst.append((-1, -1))
        while lst:
            i, j = lst.popleft()
            if i == j and i == -1:
                if lst:
                    res += 1
                    lst.append((-1, -1))
                continue
            for a, b in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= a < N and 0 <= b < M and grid[a][b] == 1:
                    grid[a][b] = 2
                    lst.append((a, b))
                    len_fresh -= 1
        return -1 if len_fresh else res

