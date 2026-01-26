# https://leetcode.com/problems/find-if-path-exists-in-graph/
# 24.01.2026


class Solution:
    def find(self, lst, n):
        if lst[n] != n:
            lst[n] = self.find(lst, lst[n])
        return lst[n]

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = list(range(n))
        for a, b in edges:
            parent[self.find(parent, b)] = self.find(parent, a)
        return self.find(parent, source) == self.find(parent, destination)

