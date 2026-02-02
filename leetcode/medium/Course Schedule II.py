# https://leetcode.com/problems/course-schedule-ii/
# 02.02.2026


class Solution: # dfs
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        d = defaultdict(list)
        for a, b in prerequisites:
            d[b].append(a)

        dd = defaultdict(int)

        def dfs(n):
            if dd[n] == 2:
                return True
            if dd[n] == 1:
                return False
            dd[n] = 1
            for nn in d[n]:
                if not dfs(nn):
                    return False
            dd[n] = 2
            res.append(n)
            return True

        for n in range(numCourses):
            if not dfs(n):
                return []
        res.reverse()
        return res


class Solution: # Kahn’s Algorithm
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1
        q = deque()
        for n in range(numCourses):
            if in_degree[n] == 0:
                q.append(n)
        while q:
            n = q.popleft()
            for nn in graph[n]:
                in_degree[nn] -= 1
                if in_degree[nn] == 0:
                    q.append(nn)
            res.append(n)
        if any(in_degree.values()):
            return []
        return res

