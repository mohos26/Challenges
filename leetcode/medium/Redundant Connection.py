# https://leetcode.com/problems/redundant-connection/
# 04.02.2026


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, n):
        if n != self.parent[n]:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        if ra == rb:
            return False

        self.parent[ra] = rb
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(max(map(max, edges))+1)
        for a, b in edges:
            if not dsu.union(a, b):
                return [a, b]
        raise ValueError("?")

