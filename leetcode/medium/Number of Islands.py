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


# 26.01.2026
class DSU:
    def __init__(self, length):
        self.parent = list(range(length))

    def find(self, n):
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def unoin(self, a, b):
        self.parent[self.find(a)] = self.find(b)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])
        dsu = DSU(M * N)
        for i in range(M):
            for j in range(N):
                idx = i * N + j
                if grid[i][j] == "1":
                    dsu.unoin(idx, idx)
                    for a, b in ((i + 1, j), (i, j + 1)):
                        if 0 <= a < M and 0 <= b < N and grid[a][b] == "1":
                            idx2 = a * N + b
                            dsu.unoin(idx, idx2)
        hash_table = set()
        for i in range(M):
            for j in range(N):
                idx = i * N + j
                if grid[i][j] == "1":
                    hash_table.add(dsu.find(idx))
        return len(hash_table)

