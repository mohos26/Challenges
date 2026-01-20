# https://leetcode.com/problems/max-area-of-island/
# 20.01.2026


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        N, M = len(grid), len(grid[0])
        def dfs(i, j):
            nonlocal tmp
            tmp += 1
            for a, b in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= a < N and 0 <= b < M and grid[a][b] == 1:
                    grid[a][b] = 0
                    dfs(a, b)
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    tmp = 0
                    grid[i][j] = 0
                    dfs(i, j)
                    res = max(res, tmp)
        return res


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        N, M = len(grid), len(grid[0])

        def bfs(i, j):
            res = 0
            d = deque([(i, j)])
            grid[i][j] = 0
            while d:
                i, j = d.popleft()
                res += 1
                for a, b in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if 0 <= a < N and 0 <= b < M and grid[a][b] == 1:
                        d.append((a, b))
                        grid[a][b] = 0
            return res

        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    res = max(res, bfs(i, j))

        return res

