# https://leetcode.com/problems/number-of-islands/
# 18.01.2026


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        def dfs(i, j):
            for a, b in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= a < len(grid) and 0 <= b < len(grid[0]) and grid[a][b] == "1":
                    grid[a][b] = "0"
                    dfs(a, b)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    res += 1
                    grid[i][j] = "0"
                    dfs(i, j)
        return res


class Solution_2:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        def bfs(i, j):
            lst = deque()
            lst.append((i, j))
            while lst:
                i, j = lst.popleft()
                for a, b in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if 0 <= a < len(grid) and 0 <= b < len(grid[0]) and grid[a][b] == "1":
                        grid[a][b] = "0"
                        lst.append((a, b))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    res += 1
                    grid[i][j] = "0"
                    bfs(i, j)
        return res

