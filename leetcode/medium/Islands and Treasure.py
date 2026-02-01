# https://neetcode.io/problems/islands-and-treasure/
# 01.02.2026


class Solution: # stander bfs
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        M, N = len(grid), len(grid[0])
        def bfs(i, j):
            q = deque()
            s = set()
            q.append((i, j, 0))
            while q:
                i, j, d = q.popleft()
                for a, b in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                    if 0 <= a < M and 0 <= b < N and grid[a][b] > 0 and (a, b) not in s:
                        grid[a][b] = min(grid[a][b], d + 1)
                        q.append((a, b, d + 1))
                        s.add((a, b))
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    bfs(i, j)


class Solution: # bfs multi-source
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        M, N = len(grid), len(grid[0])
        q = deque()
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    q.append((i, j, 0))
        while q:
            i, j, d = q.popleft()
            for a, b in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= a < M and 0 <= b < N and grid[a][b] == 2**31 - 1:
                    grid[a][b] = d + 1
                    q.append((a, b, d + 1))

