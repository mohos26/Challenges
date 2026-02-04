#
# 04.02.2026


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = defaultdict(bool)
        def dfs(n):
            if visited[n]:
                return
            visited[n] = True
            for i in graph[n]:
                dfs(i)

        res = 0
        for i in range(n):
            if not visited[i]:
                res += 1
                dfs(i)
        return res


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = defaultdict(bool)
        def bfs(n):
            d = deque([n])
            while d:
                n = d.popleft()
                visited[n] = True
                for i in graph[n]:
                    if not visited[i]:
                        d.append(i)

        res = 0
        for i in range(n):
            if not visited[i]:
                res += 1
                bfs(i)
        return res


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return
        self.count -= 1
        self.parent[rb] = ra

class Solution:
    def countComponents(self, n: int, edges):
        dsu = DSU(n)
        for a, b in edges:
            dsu.union(a, b)
        return dsu.count

