# https://neetcode.io/problems/valid-tree/
# 03.02.2026


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        d = defaultdict(list)
        for a, b in edges:
            d[a].append(b)
            d[b].append(a)
        dd = defaultdict(bool)
        def dfs(n, parent):
            if dd[n]:
                return False
            dd[n] = True
            for nn in d[n]:
                if nn != parent and not dfs(nn, n):
                    return False
            return True
        if not dfs(0, None):
            return False
        for n in range(1, n):
            if not dd[n]:
                return False
        return True

